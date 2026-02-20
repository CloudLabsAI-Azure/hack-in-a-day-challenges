"""
Intelligent Content Processing Platform - Main Streamlit Application
AI-Powered Document Pipeline: OCR → Classification → Extraction → Validation → Smart Routing
"""

import streamlit as st
import json
import os
import re
import uuid
import time
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential

from doc_processor import DocumentProcessor
from cosmos_helper import CosmosHelper

# Load environment variables
load_dotenv()

# ─── Page Configuration ──────────────────────────────────────────────
st.set_page_config(
    page_title="Intelligent Content Processing",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS Styling ─────────────────────────────────────────────────────
st.markdown(
    """
<style>
    :root {
        --primary: #0078D4;
        --secondary: #50E6FF;
        --success: #107C10;
        --warning: #F7630C;
        --error: #D13438;
    }
    .main-header {
        background: linear-gradient(135deg, #0078D4 0%, #00BCF2 50%, #50E6FF 100%);
        padding: 2rem 2.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,120,212,0.25);
    }
    .main-header h1 { color: white; margin: 0; font-size: 2.3rem; font-weight: 700; }
    .main-header p { color: rgba(255,255,255,0.9); margin: .4rem 0 0 0; font-size: 1.05rem; }
    .status-card {
        background: white; padding: 1rem 1.25rem; border-radius: 8px;
        border-left: 4px solid #0078D4; margin: .5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,.08);
    }
    .status-card.success { border-left-color: #107C10; background: #f0fff0; }
    .status-card.warning { border-left-color: #F7630C; background: #fff8f0; }
    .status-card.error   { border-left-color: #D13438; background: #fff0f0; }
    .pipeline-step {
        background: #f8f9fa; border-radius: 8px; padding: 1rem;
        border: 1px solid #e0e0e0; margin: .5rem 0;
    }
    .pipeline-step.active { border-color: #0078D4; background: #f0f7ff; }
    .pipeline-step.done   { border-color: #107C10; background: #f0fff0; }
    .review-card {
        background: white; border-radius: 8px; padding: 1.5rem;
        border: 1px solid #e0e0e0; margin: 1rem 0;
        box-shadow: 0 2px 6px rgba(0,0,0,.06);
    }
    .metric-big { font-size: 2.4rem; font-weight: 700; color: #0078D4; }
    .stButton>button {
        font-weight: 600; border-radius: 6px;
        transition: all 0.2s ease;
    }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 3px 8px rgba(0,0,0,.15); }
    [data-testid="stMetricValue"] { font-size: 2rem; font-weight: 700; color: #0078D4; }
    .stTabs [data-baseweb="tab"] { font-weight: 600; padding: .8rem 1.5rem; }
    .stTabs [aria-selected="true"] { border-bottom: 3px solid #0078D4; }
</style>
""",
    unsafe_allow_html=True,
)

# ─── Initialize Services ─────────────────────────────────────────────

doc_processor = DocumentProcessor()
cosmos = CosmosHelper()

SAMPLE_DATA = {
    "invoice_contoso": {
        "name": "Contoso Invoice (INV-2025-0847)",
        "text": """CONTOSO LTD
123 Business Avenue, Suite 400
Seattle, WA 98101

INVOICE

Invoice Number: INV-2025-0847
Invoice Date: January 15, 2025
Due Date: February 14, 2025
Payment Terms: Net 30

Bill To:
Northwind Traders
456 Commerce Street
Portland, OR 97201

Ship To:
Northwind Traders - Warehouse
789 Industrial Blvd
Portland, OR 97203

| Item Description          | Qty | Unit Price | Amount    |
|---------------------------|-----|------------|-----------|
| Office Desk - Standing    | 5   | $450.00    | $2,250.00 |
| Ergonomic Chair - Premium | 5   | $320.00    | $1,600.00 |
| Monitor Arm - Dual        | 5   | $80.00     | $400.00   |

Subtotal: $4,250.00
Tax (8.5%): $361.25
Total: $4,611.25

Payment Instructions:
Bank: First National Bank
Account: 1234567890
Routing: 021000021""",
    },
    "receipt_cafe": {
        "name": "Urban Grounds Café Receipt",
        "text": """URBAN GROUNDS CAFÉ
342 Main Street, Seattle WA
Tel: (206) 555-0147

Date: 01/15/2025  Time: 08:42 AM
Register: 03  Cashier: Maria

--------------------------------
Cappuccino Grande       $5.50
Blueberry Muffin        $3.75
Avocado Toast           $8.95
Orange Juice Fresh      $4.25
--------------------------------
Subtotal               $22.45
Tax (10.1%)             $2.27
--------------------------------
TOTAL                  $24.72

VISA ***4582
Auth: 847291

Thank you for visiting!
Rewards Points Earned: 25""",
    },
    "medical_form": {
        "name": "Patient Intake Form",
        "text": """CONTOSO MEDICAL CENTER
Patient Intake Form

Patient Information:
Full Name: Sarah Elizabeth Johnson
Date of Birth: 07/22/1990
Gender: Female
Address: 567 Oak Lane, Seattle, WA 98102
Phone: (206) 555-0234
Email: sarah.johnson@email.com
Emergency Contact: Michael Johnson (Spouse) - (206) 555-0235

Medical Record Number: MR-2025-00834

Visit Information:
Visit Date: January 20, 2025
Department: Internal Medicine
Physician: Dr. Emily Chen
Chief Complaint: Persistent headaches and fatigue for 3 weeks

Medical History:
- Asthma (diagnosed 2005)
- Seasonal allergies

Allergies: Penicillin (rash), Sulfa drugs (hives)

Current Medications:
- Albuterol inhaler (as needed)
- Cetirizine 10mg daily
- Vitamin D 2000 IU daily

Insurance Information:
Provider: Contoso Health Insurance
Policy Number: CHI-9876543
Group Number: GRP-2025-A""",
    },
    "insurance_claim": {
        "name": "Auto Insurance Claim",
        "text": """CONTOSO INSURANCE COMPANY
AUTO INSURANCE CLAIM FORM

Claim Information:
Claim Number: CLM-2025-004592
Policy Number: POL-AUTO-789012
Claim Date: January 18, 2025
Claim Type: Collision

Insured Party:
Name: David Robert Martinez
Address: 1234 Pine Street, Bellevue, WA 98004
Phone: (425) 555-0189
Email: d.martinez@email.com

Incident Details:
Date of Incident: January 17, 2025
Time of Incident: 5:45 PM
Location: Intersection of 4th Avenue and Main Street, Bellevue, WA
Police Report Number: BPD-2025-001234

Description of Incident:
While stopped at a red light at the intersection of 4th Avenue and Main Street,
the insured vehicle was rear-ended by another vehicle. The other driver admitted
fault at the scene. Minor injuries reported - neck stiffness and lower back pain.

Damage Assessment:
Items Damaged:
- Rear bumper (cracked and displaced)
- Trunk lid (dented, misaligned)
- Tail lights (both broken)
- Rear sensors (non-functional)

Estimated Repair Cost: $4,850.00
Deductible: $500.00
Estimated Payout: $4,350.00

Adjuster Information:
Adjuster Name: Lisa Wong
Adjuster ID: ADJ-5567
Assessment Date: January 19, 2025""",
    },
    "identity_doc": {
        "name": "Washington Driver's License",
        "text": """WASHINGTON STATE
DRIVER LICENSE

DL: SMITHJ*456*RQ
CLASS: C

SMITH, JOHN MICHAEL
1234 ELM STREET
SEATTLE WA 98101

DOB: 03/15/1985
ISS: 06/01/2023
EXP: 03/15/2031

SEX: M  HT: 5-11  WGT: 180
EYES: BRN  HAIR: BLK

DONOR: YES
RESTRICTIONS: CORRECTIVE LENSES""",
    },
    "poor_scan": {
        "name": "Poor Quality Scan (Test Low Confidence)",
        "text": """[SCAN QUALITY: VERY POOR - MULTIPLE ISSUES]

...Cont[illegible]...
Date: ??/??/2025

[Large smudge covering middle section]

Amount... $[smudged]...50
Reference: [cut off at edge]

...payment received from...
[ink bleed - text unreadable]

...signature: [illegible scrawl]

[Bottom third of page is blank/torn]""",
    },
}


# ─── Helper Functions ─────────────────────────────────────────────────


def validate_config():
    """Check which services are configured."""
    return {
        "agents": bool(
            os.getenv("AGENT_API_ENDPOINT") and os.getenv("AGENT_ID")
        ),
        "doc_intelligence": doc_processor.is_configured(),
        "cosmos": cosmos.is_configured(),
        "storage": bool(os.getenv("STORAGE_CONNECTION_STRING")),
    }


def upload_to_blob(file_content: bytes, filename: str) -> str:
    """Upload a file to Azure Blob Storage and return the URL."""
    try:
        from azure.storage.blob import BlobServiceClient

        conn_str = os.getenv("STORAGE_CONNECTION_STRING")
        if not conn_str:
            return ""
        blob_service = BlobServiceClient.from_connection_string(conn_str)
        container_client = blob_service.get_container_client("documents")
        blob_name = f"{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{filename}"
        container_client.upload_blob(name=blob_name, data=file_content, overwrite=True)
        return f"{blob_service.url}documents/{blob_name}"
    except Exception as e:
        st.warning(f"⚠️ Blob upload skipped: {e}")
        return ""


def _extract_json_objects(text: str) -> list:
    """Extract JSON objects from text by finding balanced braces."""
    objects = []
    i = 0
    while i < len(text):
        if text[i] == "{":
            depth = 0
            start = i
            while i < len(text):
                if text[i] == "{":
                    depth += 1
                elif text[i] == "}":
                    depth -= 1
                    if depth == 0:
                        candidate = text[start : i + 1]
                        try:
                            obj = json.loads(candidate)
                            objects.append(obj)
                        except json.JSONDecodeError:
                            pass
                        break
                i += 1
        i += 1
    return objects


def parse_pipeline_response(response_text: str) -> dict:
    """Parse the multi-agent pipeline response into structured components.

    Handles two response formats:
    1. Combined JSON: one object with classification_result, extraction_result, validation_result keys
    2. Separate blocks: individual JSON objects for each agent stage
    """
    result = {
        "classification": None,
        "extraction": None,
        "validation": None,
        "raw_response": response_text,
    }

    # Step 1: Try to extract JSON from ```json fenced blocks
    json_blocks = re.findall(r"```json\s*\n(.*?)```", response_text, re.DOTALL)
    parsed_objects = []
    for block in json_blocks:
        try:
            parsed_objects.append(json.loads(block.strip()))
        except json.JSONDecodeError:
            continue

    # Step 2: If no fenced blocks, find raw JSON objects with balanced-brace parsing
    if not parsed_objects:
        parsed_objects = _extract_json_objects(response_text)

    # Step 3: Process each parsed object
    for data in parsed_objects:
        # ── Combined response format (single JSON with all three results) ──
        if "classification_result" in data or "extraction_result" in data or "validation_result" in data:
            if "classification_result" in data:
                result["classification"] = data["classification_result"]
            if "extraction_result" in data:
                result["extraction"] = data["extraction_result"]
            if "validation_result" in data:
                vr = data["validation_result"]
                # Unwrap double-nesting if present
                if isinstance(vr, dict) and "validation_result" in vr:
                    vr = vr["validation_result"]
                result["validation"] = vr
            continue

        # ── Individual block format (separate JSON per agent) ──
        if "document_type" in data and "key_indicators" in data:
            result["classification"] = data
        elif "extracted_data" in data:
            result["extraction"] = data
        elif "validation_result" in data:
            vr = data["validation_result"]
            if isinstance(vr, dict) and "validation_result" in vr:
                vr = vr["validation_result"]
            result["validation"] = vr
        elif "confidence_score" in data and "routing_decision" in data:
            result["validation"] = data
        elif "document_type" in data:
            result["classification"] = data

    return result


def call_agent_pipeline(ocr_text: str) -> str:
    """Send OCR text through the connected agent pipeline."""
    project_endpoint = os.getenv("AGENT_API_ENDPOINT")
    agent_id = os.getenv("AGENT_ID")

    if not all([project_endpoint, agent_id]):
        st.error("❌ Agent configuration missing. Check AGENT_API_ENDPOINT and AGENT_ID.")
        return None

    try:
        client = AgentsClient(
            endpoint=project_endpoint,
            credential=DefaultAzureCredential(),
        )

        # Create thread
        thread = client.threads.create()

        # Send OCR text
        client.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"Analyze and process this document:\n\n{ocr_text}",
        )

        # Run agent pipeline (connected agents handle hand-offs automatically)
        run = client.runs.create_and_process(
            thread_id=thread.id,
            agent_id=agent_id,
        )

        if run.status == "failed":
            st.error(f"Pipeline failed: {run.last_error}")
            return None

        # Retrieve messages
        messages_response = client.messages.list(thread_id=thread.id)
        messages_list = (
            messages_response.data
            if hasattr(messages_response, "data")
            else list(messages_response)
        )

        response_text = ""
        for msg in messages_list:
            role_str = str(msg.role).lower()
            if not any(r in role_str for r in ("agent", "assistant")):
                continue
            if hasattr(msg, "text_messages") and msg.text_messages:
                for tm in msg.text_messages:
                    if hasattr(tm, "text") and hasattr(tm.text, "value"):
                        response_text += tm.text.value + "\n"
                    elif isinstance(tm, str):
                        response_text += tm + "\n"
            elif hasattr(msg, "content") and msg.content:
                for ci in msg.content:
                    ctype = str(getattr(ci, "type", "")).lower()
                    if ctype == "text":
                        text_obj = getattr(ci, "text", None)
                        if text_obj and hasattr(text_obj, "value"):
                            response_text += text_obj.value + "\n"
                        elif isinstance(text_obj, str):
                            response_text += text_obj + "\n"

        return response_text if response_text else None

    except Exception as e:
        st.error(f"❌ Pipeline error: {e}")
        return None


def route_document(parsed_result: dict, filename: str, ocr_text: str, ocr_metadata: dict, blob_url: str) -> dict:
    """Route document to the appropriate Cosmos DB container based on confidence."""
    validation = parsed_result.get("validation", {}) or {}
    classification = parsed_result.get("classification", {}) or {}

    confidence = validation.get("confidence_score", 0.0)
    routing = validation.get("routing_decision", "MANUAL_REVIEW")
    doc_type = classification.get("document_type", "UNKNOWN")

    doc_data = {
        "filename": filename,
        "doc_type": doc_type,
        "classification": classification,
        "extraction": parsed_result.get("extraction", {}),
        "validation": validation,
        "confidence_score": confidence,
        "review_reasons": validation.get("review_reasons", []),
        "ocr_text": ocr_text[:5000],  # Store first 5000 chars
        "ocr_metadata": ocr_metadata,
        "blob_url": blob_url,
    }

    routing_result = {"container": "", "doc_id": "", "routing": routing, "confidence": confidence}

    if cosmos.is_configured():
        try:
            if routing == "AUTO_APPROVE" and confidence >= 0.85:
                doc_id = cosmos.save_processed_document(doc_data)
                routing_result["container"] = "ProcessedDocuments"
                routing_result["doc_id"] = doc_id
            else:
                doc_id = cosmos.save_to_review_queue(doc_data)
                routing_result["container"] = "ReviewQueue"
                routing_result["doc_id"] = doc_id
        except Exception as e:
            st.warning(f"⚠️ Cosmos DB save failed: {e}")
    else:
        st.info("ℹ️ Cosmos DB not configured — routing result shown but not persisted.")

    return routing_result


# ─── Header ───────────────────────────────────────────────────────────
st.markdown(
    """
<div class="main-header">
    <h1>📄 Intelligent Content Processing</h1>
    <p>AI-Powered Document Pipeline — OCR → Classification → Extraction → Validation → Smart Routing</p>
</div>
""",
    unsafe_allow_html=True,
)

# ─── Sidebar ──────────────────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/200px-Microsoft_logo.svg.png",
        width=140,
    )
    st.markdown("### 🔗 Service Status")

    cfg = validate_config()
    for svc, label, icon in [
        ("agents", "AI Agents Pipeline", "🤖"),
        ("doc_intelligence", "Document Intelligence", "📝"),
        ("cosmos", "Cosmos DB", "💾"),
        ("storage", "Blob Storage", "☁️"),
    ]:
        if cfg[svc]:
            st.success(f"{icon} {label}")
        else:
            st.error(f"{icon} {label} — not configured")

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown(
        """
    This application processes documents through a multi-agent AI pipeline:

    1. **Upload** → Azure Blob Storage
    2. **OCR** → Document Intelligence
    3. **Classify** → Classification Agent
    4. **Extract** → Extraction Agent
    5. **Validate** → Validation Agent
    6. **Route** → Auto-approve or Human Review
    """
    )

# ─── Main Tabs ────────────────────────────────────────────────────────
tab_process, tab_results, tab_review, tab_analytics = st.tabs(
    ["📤 Process Documents", "📋 Processing Results", "🔍 Review Queue", "📊 Analytics"]
)

# ═══════════════════════════════════════════════════════════════════════
# TAB 1: PROCESS DOCUMENTS
# ═══════════════════════════════════════════════════════════════════════
with tab_process:
    st.markdown("## Upload & Process a Document")
    st.markdown(
        "Upload a document or select sample data. The pipeline will automatically "
        "extract text, classify, extract structured data, validate quality, and route "
        "to the appropriate container."
    )

    col_upload, col_sample = st.columns(2)

    with col_upload:
        st.markdown("### 📁 Upload a File")
        uploaded_file = st.file_uploader(
            "Drag and drop or browse",
            type=["pdf", "jpg", "jpeg", "png", "tiff", "bmp", "txt"],
            help="Supported: PDF, JPEG, PNG, TIFF, BMP, TXT",
        )

    with col_sample:
        st.markdown("### 📋 Use Sample Data")
        sample_key = st.selectbox(
            "Select a sample document",
            options=[""] + list(SAMPLE_DATA.keys()),
            format_func=lambda k: SAMPLE_DATA[k]["name"] if k else "— Select —",
        )

    st.markdown("---")

    if st.button("🚀 Process Document", type="primary", use_container_width=True):
        if not uploaded_file and not sample_key:
            st.warning("Please upload a file or select sample data first.")
        else:
            # ── Step 1: Get document content ────────────────────────
            ocr_text = ""
            ocr_metadata = {}
            filename = ""
            blob_url = ""

            progress = st.progress(0, text="Starting pipeline...")

            if sample_key:
                # Use sample data (pre-extracted OCR text)
                filename = f"{sample_key}.txt"
                sample = SAMPLE_DATA[sample_key]
                ocr_result = doc_processor.analyze_from_text(sample["text"], filename)
                ocr_text = ocr_result["extracted_text"]
                ocr_metadata = ocr_result["metadata"]
                progress.progress(15, text="✅ Sample data loaded")
            elif uploaded_file:
                filename = uploaded_file.name
                file_bytes = uploaded_file.read()

                # Upload to blob
                progress.progress(5, text="☁️ Uploading to Blob Storage...")
                blob_url = upload_to_blob(file_bytes, filename)
                progress.progress(10, text="✅ Uploaded to Blob Storage")

                # Run Document Intelligence OCR
                if doc_processor.is_configured():
                    progress.progress(15, text="📝 Running Document Intelligence OCR...")
                    ocr_result = doc_processor.analyze_document(file_bytes, filename)
                    if ocr_result["success"]:
                        ocr_text = ocr_result["extracted_text"]
                        ocr_metadata = ocr_result["metadata"]
                        progress.progress(30, text="✅ OCR extraction complete")
                    else:
                        st.error(f"OCR failed: {ocr_result['error']}")
                        st.stop()
                else:
                    # Fallback: if it's a text file, read directly
                    if filename.lower().endswith(".txt"):
                        ocr_text = file_bytes.decode("utf-8", errors="replace")
                        ocr_metadata = {"filename": filename, "source": "direct_text"}
                        progress.progress(30, text="✅ Text file loaded directly")
                    else:
                        st.error("Document Intelligence not configured. Cannot OCR this file type.")
                        st.stop()

            if not ocr_text:
                st.error("No text extracted from the document.")
                st.stop()

            # Show OCR result
            with st.expander("📝 OCR Extracted Text", expanded=False):
                st.text(ocr_text[:3000])
                if ocr_metadata:
                    st.json(ocr_metadata)

            # ── Step 2: Run agent pipeline ──────────────────────────
            progress.progress(35, text="🤖 Sending to Classification Agent...")
            time.sleep(0.5)
            progress.progress(40, text="🤖 Agent pipeline processing (Classification → Extraction → Validation)...")

            response = call_agent_pipeline(ocr_text)

            if not response:
                st.error("No response from agent pipeline.")
                st.stop()

            progress.progress(75, text="✅ Agent pipeline complete")

            # ── Step 3: Parse response ──────────────────────────────
            progress.progress(80, text="📊 Parsing pipeline results...")
            parsed = parse_pipeline_response(response)

            # ── Step 4: Route document ──────────────────────────────
            progress.progress(90, text="🔀 Routing document based on confidence...")
            routing = route_document(parsed, filename, ocr_text, ocr_metadata, blob_url)

            progress.progress(100, text="✅ Processing complete!")
            time.sleep(0.5)

            # ── Display Results ──────────────────────────────────────
            st.markdown("---")
            st.markdown("## 📊 Processing Results")

            # Routing banner
            if routing["routing"] == "AUTO_APPROVE" and routing["confidence"] >= 0.85:
                st.success(
                    f"✅ **AUTO-APPROVED** — Confidence: {routing['confidence']:.0%} — "
                    f"Saved to `ProcessedDocuments`"
                )
            else:
                st.warning(
                    f"⚠️ **SENT TO REVIEW** — Confidence: {routing['confidence']:.0%} — "
                    f"Saved to `ReviewQueue`"
                )

            # Three-column results
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### 🏷️ Classification")
                clf = parsed.get("classification")
                if clf:
                    st.metric("Document Type", clf.get("document_type", "—"))
                    st.metric("Confidence", f"{clf.get('confidence', 0):.0%}")
                    if clf.get("summary"):
                        st.info(clf["summary"])
                    if clf.get("key_indicators"):
                        st.markdown("**Key Indicators:**")
                        for ind in clf["key_indicators"]:
                            st.markdown(f"- {ind}")
                else:
                    st.warning("No classification data parsed")

            with col2:
                st.markdown("### 📋 Extraction")
                ext = parsed.get("extraction")
                if ext:
                    st.json(ext)
                else:
                    st.warning("No extraction data parsed")

            with col3:
                st.markdown("### ✅ Validation")
                val = parsed.get("validation")
                if val:
                    st.metric("Confidence Score", f"{val.get('confidence_score', 0):.0%}")
                    st.metric("Routing", val.get("routing_decision", "—"))
                    if val.get("quality_issues"):
                        st.markdown("**Issues:**")
                        for issue in val["quality_issues"]:
                            st.markdown(f"- ⚠️ {issue}")
                    if val.get("review_reasons"):
                        st.markdown("**Review Reasons:**")
                        for reason in val["review_reasons"]:
                            st.markdown(f"- 📌 {reason}")
                    if val.get("summary"):
                        st.info(val["summary"])
                else:
                    st.warning("No validation data parsed")

            # Raw response expander
            with st.expander("🔍 Raw Agent Response", expanded=False):
                st.text(response)

# ═══════════════════════════════════════════════════════════════════════
# TAB 2: PROCESSING RESULTS
# ═══════════════════════════════════════════════════════════════════════
with tab_results:
    st.markdown("## 📋 Processing History")

    if not cosmos.is_configured():
        st.info("Cosmos DB not configured. Connect Cosmos DB to see processing history.")
    else:
        docs = cosmos.get_processed_documents(limit=50)
        if not docs:
            st.info("No processed documents yet. Process some documents in the first tab!")
        else:
            st.markdown(f"**Showing {len(docs)} processed documents**")

            for doc in docs:
                with st.expander(
                    f"📄 {doc.get('filename', 'Unknown')} — "
                    f"{doc.get('docType', '?')} — "
                    f"Confidence: {doc.get('confidence_score', 0):.0%} — "
                    f"{doc.get('review_status', '?')}",
                    expanded=False,
                ):
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown(f"**Document Type:** {doc.get('docType')}")
                        st.markdown(f"**Status:** {doc.get('review_status')}")
                        st.markdown(f"**Confidence:** {doc.get('confidence_score', 0):.2%}")
                        st.markdown(f"**Timestamp:** {doc.get('timestamp', '—')}")
                    with col_b:
                        if doc.get("classification"):
                            st.markdown("**Classification:**")
                            st.json(doc["classification"])
                    if doc.get("extraction"):
                        st.markdown("**Extracted Data:**")
                        st.json(doc["extraction"])
                    if doc.get("validation"):
                        st.markdown("**Validation:**")
                        st.json(doc["validation"])

# ═══════════════════════════════════════════════════════════════════════
# TAB 3: REVIEW QUEUE
# ═══════════════════════════════════════════════════════════════════════
with tab_review:
    st.markdown("## 🔍 Documents Pending Review")
    st.markdown(
        "These documents had confidence scores below 0.85 and need human verification. "
        "Review the extracted data and approve or reject each document."
    )

    if not cosmos.is_configured():
        st.info("Cosmos DB not configured. Connect Cosmos DB to use the review queue.")
    else:
        # Filter selector
        review_filter = st.selectbox(
            "Show:",
            ["PENDING", "REJECTED", "ALL"],
            index=0,
        )
        review_docs = cosmos.get_review_queue(status=review_filter)

        if not review_docs:
            st.success("🎉 No documents pending review!" if review_filter == "PENDING" else "No documents found.")
        else:
            st.markdown(f"**{len(review_docs)} document(s) found**")

            for doc in review_docs:
                st.markdown("---")
                st.markdown(
                    f"""<div class="review-card">
                    <h4>📄 {doc.get('filename', 'Unknown')} — {doc.get('docType', '?')}</h4>
                    <p>Confidence: <strong>{doc.get('confidence_score', 0):.0%}</strong> | 
                    Status: <strong>{doc.get('review_status', '?')}</strong> |
                    Submitted: {doc.get('timestamp', '—')}</p>
                    </div>""",
                    unsafe_allow_html=True,
                )

                # Show review reasons
                reasons = doc.get("review_reasons", [])
                if reasons:
                    st.markdown("**⚠️ Review Reasons:**")
                    for r in reasons:
                        st.markdown(f"- {r}")

                # Show extracted data
                col_clf, col_ext, col_val = st.columns(3)
                with col_clf:
                    st.markdown("**Classification:**")
                    st.json(doc.get("classification", {}))
                with col_ext:
                    st.markdown("**Extracted Data:**")
                    st.json(doc.get("extraction", {}))
                with col_val:
                    st.markdown("**Validation:**")
                    st.json(doc.get("validation", {}))

                # OCR text
                ocr = doc.get("ocr_text", "")
                if ocr:
                    with st.expander("📝 Original OCR Text"):
                        st.text(ocr[:2000])

                # Action buttons (only for PENDING)
                if doc.get("review_status") == "PENDING":
                    col_approve, col_reject = st.columns(2)
                    with col_approve:
                        if st.button(f"✅ Approve", key=f"approve_{doc['id']}"):
                            if cosmos.approve_document(doc["id"]):
                                st.success("Document approved and moved to ProcessedDocuments!")
                                st.rerun()
                            else:
                                st.error("Approval failed.")
                    with col_reject:
                        reason = st.text_input(
                            "Rejection reason",
                            key=f"reason_{doc['id']}",
                            placeholder="e.g., Document is illegible, rescan required",
                        )
                        if st.button(f"❌ Reject", key=f"reject_{doc['id']}"):
                            if cosmos.reject_document(doc["id"], reason):
                                st.warning("Document rejected.")
                                st.rerun()
                            else:
                                st.error("Rejection failed.")

                elif doc.get("review_status") == "REJECTED":
                    st.error(f"**Rejected** — Reason: {doc.get('rejection_reason', 'No reason provided')}")

# ═══════════════════════════════════════════════════════════════════════
# TAB 4: ANALYTICS
# ═══════════════════════════════════════════════════════════════════════
with tab_analytics:
    st.markdown("## 📊 Processing Analytics")

    if not cosmos.is_configured():
        st.info("Cosmos DB not configured. Connect Cosmos DB to see analytics.")
    else:
        analytics = cosmos.get_analytics()

        # Top-level metrics
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Total Processed", analytics["total_processed"])
        m2.metric("Auto-Approved", analytics["auto_approved"])
        m3.metric("Human Approved", analytics["human_approved"])
        m4.metric("Pending Review", analytics["pending_review"])
        m5.metric("Rejected", analytics["rejected"])

        st.markdown("---")

        col_charts1, col_charts2 = st.columns(2)

        with col_charts1:
            st.markdown("### Document Type Distribution")
            dist = analytics.get("doc_type_distribution", {})
            if dist:
                df_types = pd.DataFrame(
                    list(dist.items()), columns=["Document Type", "Count"]
                )
                st.bar_chart(df_types.set_index("Document Type"))
            else:
                st.info("No data yet.")

        with col_charts2:
            st.markdown("### Confidence Score Distribution")
            scores = analytics.get("confidence_scores", [])
            if scores:
                df_scores = pd.DataFrame(scores, columns=["Confidence"])
                st.bar_chart(df_scores["Confidence"].value_counts().sort_index())
            else:
                st.info("No data yet.")

        # Average confidence
        st.markdown("---")
        avg_col1, avg_col2 = st.columns(2)
        with avg_col1:
            st.metric(
                "Average Confidence Score",
                f"{analytics['avg_confidence']:.1%}",
            )
        with avg_col2:
            total = analytics["total_processed"]
            if total > 0:
                approval_rate = (
                    analytics["auto_approved"] + analytics["human_approved"]
                ) / total
                st.metric("Overall Approval Rate", f"{approval_rate:.0%}")

        # Export button
        st.markdown("---")
        if analytics["total_processed"] > 0:
            all_docs = cosmos.get_all_documents()
            if all_docs:
                export_data = []
                for d in all_docs:
                    export_data.append(
                        {
                            "filename": d.get("filename", ""),
                            "doc_type": d.get("docType", ""),
                            "confidence_score": d.get("confidence_score", 0),
                            "routing_decision": d.get("routing_decision", ""),
                            "review_status": d.get("review_status", ""),
                            "timestamp": d.get("timestamp", ""),
                        }
                    )
                df_export = pd.DataFrame(export_data)
                csv = df_export.to_csv(index=False)
                st.download_button(
                    "📥 Export Processing Report (CSV)",
                    data=csv,
                    file_name=f"content_processing_report_{datetime.utcnow().strftime('%Y%m%d')}.csv",
                    mime="text/csv",
                )
