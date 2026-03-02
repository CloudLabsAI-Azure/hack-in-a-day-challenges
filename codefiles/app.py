"""
AI-Powered Data Security & Compliance Agent
Streamlit Dashboard Application
"""

import streamlit as st
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from azure.cosmos import CosmosClient, exceptions
import uuid
import re
import time
import pandas as pd
from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential

load_dotenv()

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Data Security Agent",
    page_icon="shield",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------------------------
# Configuration validation
# ---------------------------------------------------------------------------
def validate_configuration():
    required_vars = {
        "AGENT_API_ENDPOINT": os.getenv("AGENT_API_ENDPOINT"),
        "AGENT_ID": os.getenv("AGENT_ID"),
    }
    optional_vars = {
        "COSMOS_ENDPOINT": os.getenv("COSMOS_ENDPOINT"),
        "COSMOS_KEY": os.getenv("COSMOS_KEY"),
        "STORAGE_ACCOUNT_NAME": os.getenv("STORAGE_ACCOUNT_NAME"),
        "STORAGE_ACCOUNT_KEY": os.getenv("STORAGE_ACCOUNT_KEY"),
        "EVENT_GRID_ENDPOINT": os.getenv("EVENT_GRID_ENDPOINT"),
        "EVENT_GRID_KEY": os.getenv("EVENT_GRID_KEY"),
    }
    missing_required = [k for k, v in required_vars.items() if not v or v.strip() == ""]
    missing_optional = [k for k, v in optional_vars.items() if not v or v.strip() == ""]
    return missing_required, missing_optional


def show_setup_guide(missing_required, missing_optional):
    st.error("Configuration Required")
    st.markdown("""
    ### Setup Guide

    Edit the `.env` file in the codefiles folder with your credentials.
    """)
    if missing_required:
        st.warning(f"**Missing required variables:** {', '.join(missing_required)}")
    if missing_optional:
        st.info(f"**Missing optional variables (some features disabled):** {', '.join(missing_optional)}")
    st.stop()


missing_required, missing_optional = validate_configuration()
if missing_required:
    show_setup_guide(missing_required, missing_optional)

# ---------------------------------------------------------------------------
# CSS Styling & Animations
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    /* ---- Animated Gradient Header ---- */
    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .main-header {
        background: linear-gradient(-45deg, #0F62FE, #6366F1, #0F62FE, #A855F7);
        background-size: 400% 400%;
        animation: gradientShift 10s ease infinite;
        padding: 2rem 2.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(15,98,254,0.18);
    }
    .main-header h1 { color: #fff; margin: 0; font-size: 2.2rem; font-weight: 700; letter-spacing: -0.5px; }
    .main-header p  { color: rgba(255,255,255,0.85); margin: 0.4rem 0 0; font-size: 1.05rem; }

    /* ---- Fade-in animation ---- */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(18px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .fade-in { animation: fadeInUp 0.5s ease-out; }

    /* ---- Status pulse ---- */
    @keyframes statusPulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(16,185,129,0.35); }
        50%      { box-shadow: 0 0 0 8px rgba(16,185,129,0); }
    }
    .status-dot-ok {
        display: inline-block; width: 10px; height: 10px; border-radius: 50%;
        background: #10B981; animation: statusPulse 2s infinite; margin-right: 6px;
    }
    .status-dot-warn {
        display: inline-block; width: 10px; height: 10px; border-radius: 50%;
        background: #F59E0B; margin-right: 6px;
    }
    .status-dot-off {
        display: inline-block; width: 10px; height: 10px; border-radius: 50%;
        background: #EF4444; margin-right: 6px;
    }

    /* ---- Metric cards ---- */
    .metric-card {
        background: #fff; border-radius: 10px; padding: 1.2rem 1.5rem;
        border: 1px solid #E5E7EB; box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        animation: fadeInUp 0.5s ease-out;
    }
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.10);
    }
    .metric-card .label { font-size: 0.82rem; color: #6B7280; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 0.3rem; }
    .metric-card .value { font-size: 1.8rem; font-weight: 700; color: #111827; }

    /* severity colors */
    .sev-critical { border-left: 4px solid #EF4444; }
    .sev-high     { border-left: 4px solid #F97316; }
    .sev-medium   { border-left: 4px solid #F59E0B; }
    .sev-low      { border-left: 4px solid #10B981; }

    .badge {
        display: inline-block; padding: 3px 10px; border-radius: 6px;
        font-size: 0.75rem; font-weight: 600; color: #fff; letter-spacing: 0.3px;
    }
    .badge-critical { background: #EF4444; }
    .badge-high     { background: #F97316; }
    .badge-medium   { background: #F59E0B; color: #111; }
    .badge-low      { background: #10B981; }
    .badge-pii      { background: #EF4444; }
    .badge-phi      { background: #8B5CF6; }
    .badge-pci      { background: #F97316; }
    .badge-conf     { background: #F59E0B; color: #111; }
    .badge-public   { background: #10B981; }

    /* ---- Completion banner ---- */
    .completion-banner {
        padding: 1.2rem; border-radius: 10px; text-align: center; margin: 1rem 0;
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        box-shadow: 0 4px 16px rgba(16,185,129,0.25);
        animation: fadeInUp 0.5s ease-out;
    }
    .completion-banner h3 { margin: 0; color: #fff; font-size: 1.15rem; }
    .completion-banner p  { margin: 0.3rem 0 0; color: rgba(255,255,255,0.9); font-size: 0.92rem; }

    /* ---- Buttons ---- */
    .stButton>button {
        background: linear-gradient(135deg, #0F62FE 0%, #6366F1 100%);
        color: #fff; font-weight: 600; border: none; padding: 0.7rem 1.8rem;
        border-radius: 8px; transition: all 0.25s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(15,98,254,0.3);
    }

    /* ---- Sidebar ---- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
    }
    [data-testid="stSidebar"] * { color: #E2E8F0 !important; }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stRadio label { color: #E2E8F0 !important; }

    /* ---- Tabs ---- */
    .stTabs [data-baseweb="tab-list"] { gap: 0.5rem; }
    .stTabs [data-baseweb="tab"] {
        background: #F3F4F6; border-radius: 8px 8px 0 0;
        padding: 0.8rem 1.4rem; font-weight: 600; font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background: #fff; border-bottom: 3px solid #0F62FE;
    }

    /* ---- Progress ---- */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #0F62FE 0%, #A855F7 100%);
    }

    /* ---- Risk row animation ---- */
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-12px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    .risk-row { animation: slideIn 0.4s ease-out; }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Cosmos DB connection
# ---------------------------------------------------------------------------
@st.cache_resource
def get_cosmos_client():
    try:
        endpoint = os.getenv("COSMOS_ENDPOINT")
        key = os.getenv("COSMOS_KEY")
        db_name = os.getenv("DATABASE_NAME", "SecurityAgentDB")
        if not all([endpoint, key, db_name]):
            return None, None, None, None
        client = CosmosClient(endpoint, credential=key)
        database = client.get_database_client(db_name)
        scan_container = database.get_container_client("ScanResults")
        alerts_container = database.get_container_client("SecurityAlerts")
        return client, database, scan_container, alerts_container
    except Exception as e:
        return None, None, None, None


def save_scan_to_cosmos(scan_data: dict):
    _, _, scan_container, _ = get_cosmos_client()
    if not scan_container:
        return None
    try:
        item = {
            "id": str(uuid.uuid4()),
            "scanId": scan_data.get("scan_id", str(uuid.uuid4())),
            "scanType": scan_data.get("scan_type", "fast"),
            "timestamp": datetime.utcnow().isoformat(),
            "datasets_scanned": scan_data.get("datasets_scanned", []),
            "classification": scan_data.get("classification", {}),
            "risks": scan_data.get("risks", {}),
            "compliance": scan_data.get("compliance", {}),
            "risk_summary": scan_data.get("risk_summary", {}),
            "compliance_score": scan_data.get("compliance_score", 0),
            "raw_response": scan_data.get("raw_response", "")
        }
        scan_container.create_item(body=item)
        return item["id"]
    except Exception as e:
        return None


def save_alert_to_cosmos(alert: dict):
    _, _, _, alerts_container = get_cosmos_client()
    if not alerts_container:
        return None
    try:
        item = {
            "id": str(uuid.uuid4()),
            "severity": alert.get("severity", "MEDIUM"),
            "risk_id": alert.get("risk_id", ""),
            "description": alert.get("description", ""),
            "affected_resource": alert.get("affected_resource", ""),
            "status": "NEW",
            "timestamp": datetime.utcnow().isoformat()
        }
        alerts_container.create_item(body=item)
        return item["id"]
    except Exception:
        return None


def get_scan_history(limit=20):
    _, _, scan_container, _ = get_cosmos_client()
    if not scan_container:
        return []
    try:
        return list(scan_container.query_items(
            query=f"SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT {limit}",
            enable_cross_partition_query=True
        ))
    except Exception:
        return []


def get_alerts(severity_filter=None, limit=50):
    _, _, _, alerts_container = get_cosmos_client()
    if not alerts_container:
        return []
    try:
        if severity_filter and severity_filter != "ALL":
            query = f"SELECT * FROM c WHERE c.severity = '{severity_filter}' ORDER BY c.timestamp DESC OFFSET 0 LIMIT {limit}"
        else:
            query = f"SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT {limit}"
        return list(alerts_container.query_items(query=query, enable_cross_partition_query=True))
    except Exception:
        return []

# ---------------------------------------------------------------------------
# Event Grid publishing
# ---------------------------------------------------------------------------
def publish_to_event_grid(risks: list):
    """Publish CRITICAL/HIGH risks to Event Grid. Returns (published, skipped) counts."""
    endpoint = os.getenv("EVENT_GRID_ENDPOINT")
    key = os.getenv("EVENT_GRID_KEY")
    if not endpoint or not key:
        return 0, len(risks)
    try:
        from azure.eventgrid import EventGridPublisherClient, EventGridEvent
        from azure.core.credentials import AzureKeyCredential

        client = EventGridPublisherClient(endpoint=endpoint, credential=AzureKeyCredential(key))
        published, skipped = 0, 0
        for risk in risks:
            sev = risk.get("severity", "LOW")
            if sev in ["CRITICAL", "HIGH"]:
                event = EventGridEvent(
                    id=str(uuid.uuid4()),
                    event_type="DataSecurity.RiskDetected",
                    subject=f"/security/risks/{risk.get('risk_id', 'unknown')}",
                    data={
                        "risk_id": risk.get("risk_id", ""),
                        "severity": sev,
                        "category": risk.get("category", ""),
                        "description": risk.get("description", ""),
                        "affected_resource": risk.get("affected_resource", ""),
                        "detected_at": datetime.utcnow().isoformat(),
                        "source": "AI-Data-Security-Agent"
                    },
                    data_version="1.0"
                )
                client.send([event])
                published += 1

                # Also save alert to Cosmos DB directly
                save_alert_to_cosmos(risk)
            else:
                skipped += 1
        return published, skipped
    except Exception as e:
        return 0, len(risks)

# ---------------------------------------------------------------------------
# Storage Account helpers
# ---------------------------------------------------------------------------
def load_from_storage(container: str, blob: str):
    """Load a file from Azure Blob Storage. Falls back to local datasets/ folder."""
    acct = os.getenv("STORAGE_ACCOUNT_NAME")
    key = os.getenv("STORAGE_ACCOUNT_KEY")
    if acct and key:
        try:
            from azure.storage.blob import BlobServiceClient
            conn = f"DefaultEndpointsProtocol=https;AccountName={acct};AccountKey={key};EndpointSuffix=core.windows.net"
            svc = BlobServiceClient.from_connection_string(conn)
            bc = svc.get_blob_client(container=container, blob=blob)
            data = bc.download_blob().readall().decode("utf-8")
            if blob.endswith(".json"):
                return json.loads(data)
            return data
        except Exception:
            pass

    # Fallback: local datasets folder
    local_path = os.path.join(os.path.dirname(__file__), "datasets", blob)
    if os.path.exists(local_path):
        with open(local_path, "r", encoding="utf-8") as f:
            if blob.endswith(".json"):
                return json.load(f)
            return f.read()
    return None

# ---------------------------------------------------------------------------
# Agent response parsing
# ---------------------------------------------------------------------------
def parse_agent_response(response_text: str) -> dict:
    """Parse the combined response from the 3-agent pipeline."""
    result = {
        "classification": None,
        "risks": None,
        "compliance": None,
    }

    json_blocks = re.findall(r'```json\n(.*?)```', response_text, re.DOTALL)
    for block in json_blocks:
        try:
            data = json.loads(block)
            # Classification output
            if any(k in data for k in ("columns", "classifications", "sensitivity_map", "classified_columns")):
                result["classification"] = data
            # Risk output
            elif any(k in data for k in ("risks", "risk_summary", "risk_findings")):
                result["risks"] = data
            # Compliance output
            elif any(k in data for k in ("remediation_plan", "compliance_mapping", "compliance_score", "remediation")):
                result["compliance"] = data
            # Generic — assign to first empty slot
            elif result["classification"] is None:
                result["classification"] = data
            elif result["risks"] is None:
                result["risks"] = data
            elif result["compliance"] is None:
                result["compliance"] = data
        except json.JSONDecodeError:
            continue

    # Fallback: look for JSON objects without code fences
    if not any(result.values()):
        json_objs = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', response_text)
        for obj_str in json_objs:
            try:
                data = json.loads(obj_str)
                if len(data) > 1:
                    if result["classification"] is None:
                        result["classification"] = data
                    elif result["risks"] is None:
                        result["risks"] = data
                    elif result["compliance"] is None:
                        result["compliance"] = data
            except json.JSONDecodeError:
                continue

    return result

# ---------------------------------------------------------------------------
# Agent API call
# ---------------------------------------------------------------------------
def call_agent_api(prompt: str):
    """Call Azure AI Foundry Agent via AgentsClient SDK."""
    try:
        project_endpoint = os.getenv("AGENT_API_ENDPOINT")
        agent_id = os.getenv("AGENT_ID")
        if not all([project_endpoint, agent_id]):
            st.error("Missing agent configuration. Check your .env file.")
            return None

        with st.spinner("Connecting to Azure AI Foundry ..."):
            client = AgentsClient(endpoint=project_endpoint, credential=DefaultAzureCredential())

        with st.spinner("Creating conversation thread ..."):
            thread = client.threads.create()
            thread_id = thread.id

        with st.spinner("Sending data to Classification Agent ..."):
            client.messages.create(thread_id=thread_id, role="user", content=prompt)

        with st.spinner("Running agent pipeline — Classification, Risk Detection, Compliance ..."):
            run = client.runs.create_and_process(thread_id=thread_id, agent_id=agent_id)

        if run.status == "failed":
            st.error(f"Agent run failed: {run.last_error}")
            return None

        with st.spinner("Retrieving results ..."):
            messages_response = client.messages.list(thread_id=thread_id)
            messages_list = messages_response.data if hasattr(messages_response, "data") else list(messages_response)

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
                    ct = str(getattr(ci, "type", "")).lower()
                    if ct == "text":
                        txt = getattr(ci, "text", None)
                        if txt is not None:
                            if hasattr(txt, "value"):
                                response_text += txt.value + "\n"
                            elif isinstance(txt, str):
                                response_text += txt + "\n"

        if not response_text.strip():
            st.error("No response received from agents.")
            return None

        return response_text

    except Exception as e:
        st.error(f"Error calling agent: {str(e)}")
        with st.expander("Error Details"):
            import traceback
            st.code(traceback.format_exc())
        return None

# ---------------------------------------------------------------------------
# Build scan prompt
# ---------------------------------------------------------------------------
def build_scan_prompt(datasets: list, access_policies, access_logs, scan_mode: str, row_limit: int) -> str:
    """Construct the prompt sent to the Classification Agent."""
    parts = [
        f"Analyze the following data assets for security classification, risk detection, and compliance.\n",
        f"SCAN MODE: {'Fast Scan (sample rows only)' if scan_mode == 'Fast' else 'Full Scan (all available rows)'}\n",
    ]

    for ds in datasets:
        if ds:
            table = ds.get("table_name", "Unknown")
            db = ds.get("database", "Unknown")
            total = ds.get("total_rows", "unknown")
            cols = ds.get("columns", [])
            rows = ds.get("sample_rows", [])
            if scan_mode == "Fast" and len(rows) > row_limit:
                rows = rows[:row_limit]

            parts.append(f"\n--- DATA ASSET: {table} (Database: {db}, Total Rows: {total}) ---")
            parts.append(f"Schema:\n```json\n{json.dumps(cols, indent=2)}\n```")
            parts.append(f"Sample Data ({len(rows)} rows):\n```json\n{json.dumps(rows, indent=2)}\n```")

    if access_policies:
        parts.append(f"\n--- ACCESS POLICIES ---\n```json\n{json.dumps(access_policies, indent=2)}\n```")

    if access_logs:
        if isinstance(access_logs, str):
            parts.append(f"\n--- ACCESS LOGS ---\n```\n{access_logs}\n```")
        elif isinstance(access_logs, list):
            parts.append(f"\n--- ACCESS LOGS ({len(access_logs)} entries) ---\n```\n{json.dumps(access_logs[:50], indent=2)}\n```")

    parts.append("\nPerform a comprehensive security analysis following your instructions.")

    return "\n".join(parts)

# ---------------------------------------------------------------------------
# Helper renderers
# ---------------------------------------------------------------------------
def severity_badge(sev: str) -> str:
    s = sev.upper()
    cls = {"CRITICAL": "badge-critical", "HIGH": "badge-high", "MEDIUM": "badge-medium", "LOW": "badge-low"}.get(s, "badge-low")
    return f'<span class="badge {cls}">{s}</span>'


def classification_badge(cls_name: str) -> str:
    c = cls_name.upper()
    badge = {"PII": "badge-pii", "PHI": "badge-phi", "PCI": "badge-pci", "CONFIDENTIAL": "badge-conf", "PUBLIC": "badge-public"}.get(c, "badge-public")
    return f'<span class="badge {badge}">{c}</span>'


def render_metric_card(label: str, value, extra_class: str = ""):
    return f"""
    <div class="metric-card {extra_class}">
        <div class="label">{label}</div>
        <div class="value">{value}</div>
    </div>"""

# ===========================================================================
# HEADER
# ===========================================================================
st.markdown("""
<div class="main-header">
    <h1>Data Security & Compliance Agent</h1>
    <p>Identify sensitive data, detect risky access patterns, and generate compliance recommendations</p>
</div>
""", unsafe_allow_html=True)

# ===========================================================================
# SIDEBAR
# ===========================================================================
with st.sidebar:
    st.markdown("### Connection Status")

    endpoint = os.getenv("AGENT_API_ENDPOINT")
    agent_id = os.getenv("AGENT_ID")
    cosmos_ep = os.getenv("COSMOS_ENDPOINT")
    storage_name = os.getenv("STORAGE_ACCOUNT_NAME")
    eg_ep = os.getenv("EVENT_GRID_ENDPOINT")

    def status_dot(ok):
        return '<span class="status-dot-ok"></span>' if ok else '<span class="status-dot-off"></span>'

    st.markdown(f'{status_dot(endpoint and agent_id)} AI Foundry Agents', unsafe_allow_html=True)
    st.markdown(f'{status_dot(cosmos_ep)} Cosmos DB', unsafe_allow_html=True)
    st.markdown(f'{status_dot(storage_name)} Storage Account', unsafe_allow_html=True)
    st.markdown(f'{status_dot(eg_ep)} Event Grid', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Scan Settings")
    scan_mode = st.radio("Scan Mode", ["Fast", "Full"], index=0,
                         help="Fast: top 5 rows per table. Full: all available sample rows.")
    fast_row_limit = 5

    st.markdown("---")
    st.markdown("### Stats")
    history = get_scan_history(limit=100)
    st.metric("Total Scans", len(history))
    alerts_all = get_alerts(limit=100)
    st.metric("Active Alerts", sum(1 for a in alerts_all if a.get("status") == "NEW"))

# ===========================================================================
# TABS
# ===========================================================================
tab_scan, tab_class, tab_risks, tab_fix, tab_alerts, tab_history = st.tabs([
    "Scan Data Assets",
    "Classification",
    "Risk Detection",
    "Remediation",
    "Alerts & Approvals",
    "Scan History"
])

# ---------------------------------------------------------------------------
# TAB 1: Scan Data Assets
# ---------------------------------------------------------------------------
with tab_scan:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### Select Data Sources")

    col_left, col_right = st.columns([3, 1])
    with col_left:
        available_datasets = {
            "customer_data.json": "Customers (RetailDB)",
            "medical_records.json": "Medical Records (HealthcareDB)",
            "financial_transactions.json": "Financial Transactions (FinanceDB)",
            "employee_data.json": "Employees (HRDB)"
        }
        selected_files = st.multiselect(
            "Choose datasets to scan",
            options=list(available_datasets.keys()),
            default=list(available_datasets.keys()),
            format_func=lambda x: available_datasets[x]
        )
        include_policies = st.checkbox("Include access policies", value=True)
        include_logs = st.checkbox("Include access logs", value=True)

    with col_right:
        st.markdown(f"**Mode:** {scan_mode} Scan")
        if scan_mode == "Fast":
            st.caption(f"Reads top {fast_row_limit} rows per table")
        else:
            st.caption("Reads all available sample rows")
        st.markdown(f"**Datasets:** {len(selected_files)} selected")

    st.markdown("---")

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        run_scan = st.button("Run Security Scan", type="primary", use_container_width=True)

    if run_scan:
        if not selected_files:
            st.error("Select at least one dataset to scan.")
        else:
            # Load datasets
            datasets = []
            progress = st.progress(0, text="Loading data sources ...")
            for i, fname in enumerate(selected_files):
                ds = load_from_storage("schemas", fname)
                if ds:
                    datasets.append(ds)
                progress.progress((i + 1) / (len(selected_files) + 2), text=f"Loaded {fname}")

            access_policies = None
            if include_policies:
                access_policies = load_from_storage("access-policies", "access_policies.json")
                progress.progress((len(selected_files) + 1) / (len(selected_files) + 2), text="Loaded access policies")

            access_logs = None
            if include_logs:
                access_logs = load_from_storage("access-logs", "access_logs.csv")
                progress.progress(1.0, text="Loaded access logs")

            time.sleep(0.3)
            progress.empty()

            # Build prompt
            prompt = build_scan_prompt(
                datasets=datasets,
                access_policies=access_policies,
                access_logs=access_logs,
                scan_mode=scan_mode,
                row_limit=fast_row_limit
            )

            # Call agent pipeline
            response_text = call_agent_api(prompt)

            if response_text:
                parsed = parse_agent_response(response_text)

                # Extract risk list for Event Grid
                risk_list = []
                if parsed["risks"]:
                    risk_list = parsed["risks"].get("risks", parsed["risks"].get("risk_findings", []))

                # Publish critical/high risks to Event Grid
                pub_count, skip_count = 0, 0
                if risk_list:
                    pub_count, skip_count = publish_to_event_grid(risk_list)

                # Save to Cosmos DB
                scan_result = {
                    "scan_id": str(uuid.uuid4()),
                    "scan_type": scan_mode.lower(),
                    "datasets_scanned": selected_files,
                    "classification": parsed["classification"],
                    "risks": parsed["risks"],
                    "compliance": parsed["compliance"],
                    "risk_summary": parsed["risks"].get("risk_summary", {}) if parsed["risks"] else {},
                    "compliance_score": parsed["compliance"].get("compliance_score", 0) if parsed["compliance"] else 0,
                    "raw_response": response_text
                }
                cosmos_id = save_scan_to_cosmos(scan_result)

                # Store in session
                st.session_state["last_scan"] = scan_result
                st.session_state["last_scan_raw"] = response_text

                # Completion banner
                st.markdown(f"""
                <div class="completion-banner">
                    <h3>Scan Complete</h3>
                    <p>{len(selected_files)} datasets analyzed &nbsp;|&nbsp; {pub_count} alerts published to Event Grid &nbsp;|&nbsp; {'Saved to Cosmos DB' if cosmos_id else 'Cosmos DB not connected'}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# TAB 2: Classification
# ---------------------------------------------------------------------------
with tab_class:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### Data Classification Results")

    scan = st.session_state.get("last_scan")
    if scan and scan.get("classification"):
        cls_data = scan["classification"]

        # Try to extract column-level classifications
        columns = cls_data.get("columns", cls_data.get("classifications", cls_data.get("classified_columns", [])))

        if isinstance(columns, list) and columns:
            # Count by category
            counts = {}
            for col in columns:
                cat = col.get("classification", col.get("category", col.get("sensitivity", "PUBLIC"))).upper()
                counts[cat] = counts.get(cat, 0) + 1

            # Metric cards
            mc1, mc2, mc3, mc4, mc5 = st.columns(5)
            with mc1:
                st.markdown(render_metric_card("Total Columns", len(columns)), unsafe_allow_html=True)
            with mc2:
                st.markdown(render_metric_card("PII", counts.get("PII", 0), "sev-critical"), unsafe_allow_html=True)
            with mc3:
                st.markdown(render_metric_card("PHI", counts.get("PHI", 0), "sev-high"), unsafe_allow_html=True)
            with mc4:
                st.markdown(render_metric_card("PCI", counts.get("PCI", 0), "sev-medium"), unsafe_allow_html=True)
            with mc5:
                st.markdown(render_metric_card("Public", counts.get("PUBLIC", 0), "sev-low"), unsafe_allow_html=True)

            st.markdown("---")

            # Table
            rows_display = []
            for col in columns:
                cat = col.get("classification", col.get("category", col.get("sensitivity", "PUBLIC"))).upper()
                rows_display.append({
                    "Table": col.get("table", col.get("table_name", "")),
                    "Column": col.get("column_name", col.get("column", col.get("name", ""))),
                    "Type": col.get("data_type", col.get("type", "")),
                    "Classification": cat,
                    "Confidence": col.get("confidence", ""),
                    "Regulation": ", ".join(col.get("regulation", col.get("regulations", []))) if isinstance(col.get("regulation", col.get("regulations", [])), list) else str(col.get("regulation", "")),
                    "Action": col.get("recommended_action", col.get("action", ""))
                })

            df = pd.DataFrame(rows_display)
            st.dataframe(df, use_container_width=True, height=400)
        else:
            # Show raw classification JSON
            st.json(cls_data)

        with st.expander("Raw Classification Output"):
            st.json(cls_data)
    else:
        st.info("Run a security scan first to see classification results.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# TAB 3: Risk Detection
# ---------------------------------------------------------------------------
with tab_risks:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### Risk Detection Results")

    scan = st.session_state.get("last_scan")
    if scan and scan.get("risks"):
        risk_data = scan["risks"]
        risk_list = risk_data.get("risks", risk_data.get("risk_findings", []))

        # Summary
        summary = risk_data.get("risk_summary", {})
        if not summary and isinstance(risk_list, list):
            summary = {}
            for r in risk_list:
                s = r.get("severity", "LOW").upper()
                summary[s.lower()] = summary.get(s.lower(), 0) + 1

        rc1, rc2, rc3, rc4 = st.columns(4)
        with rc1:
            st.markdown(render_metric_card("Critical", summary.get("critical", summary.get("CRITICAL", 0)), "sev-critical"), unsafe_allow_html=True)
        with rc2:
            st.markdown(render_metric_card("High", summary.get("high", summary.get("HIGH", 0)), "sev-high"), unsafe_allow_html=True)
        with rc3:
            st.markdown(render_metric_card("Medium", summary.get("medium", summary.get("MEDIUM", 0)), "sev-medium"), unsafe_allow_html=True)
        with rc4:
            st.markdown(render_metric_card("Low", summary.get("low", summary.get("LOW", 0)), "sev-low"), unsafe_allow_html=True)

        st.markdown("---")

        # Compliance score if present
        comp_score = risk_data.get("compliance_score")
        if comp_score is not None:
            st.markdown(f"**Compliance Score:** {comp_score}")
            st.progress(min(float(comp_score) / 100 if float(comp_score) > 1 else float(comp_score), 1.0))

        # Risk list
        if isinstance(risk_list, list):
            for i, risk in enumerate(risk_list):
                sev = risk.get("severity", "LOW").upper()
                sev_class = f"sev-{sev.lower()}"
                st.markdown(f"""
                <div class="metric-card {sev_class} risk-row" style="margin-bottom:0.8rem;">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <div>
                            {severity_badge(sev)}
                            <strong style="margin-left:8px;">{risk.get('risk_id', risk.get('id', f'RISK-{i+1:03d}'))}</strong>
                            — <span style="color:#6B7280;">{risk.get('category', '')}</span>
                        </div>
                        <span style="font-size:0.82rem;color:#9CA3AF;">{risk.get('affected_resource', risk.get('affected_data_classification', ''))}</span>
                    </div>
                    <p style="margin:0.5rem 0 0;color:#374151;">{risk.get('description', '')}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.json(risk_data)

        with st.expander("Raw Risk Output"):
            st.json(risk_data)
    else:
        st.info("Run a security scan first to see risk detection results.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# TAB 4: Remediation & Compliance
# ---------------------------------------------------------------------------
with tab_fix:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### Remediation & Compliance")

    scan = st.session_state.get("last_scan")
    if scan and scan.get("compliance"):
        comp_data = scan["compliance"]

        # Compliance score
        score = comp_data.get("compliance_score", comp_data.get("score", None))
        if score is not None:
            sc1, sc2 = st.columns([1, 3])
            with sc1:
                st.markdown(render_metric_card("Compliance Score", f"{score}{'%' if float(str(score)) > 1 else ''}"), unsafe_allow_html=True)
            with sc2:
                score_val = float(str(score))
                normalized = score_val / 100 if score_val > 1 else score_val
                st.progress(min(normalized, 1.0))

        st.markdown("---")

        # Remediation plans
        remediation = comp_data.get("remediation_plan", comp_data.get("remediation", comp_data.get("recommendations", [])))
        if isinstance(remediation, list) and remediation:
            st.markdown("#### Remediation Steps")
            for idx, item in enumerate(remediation):
                if isinstance(item, dict):
                    approval = item.get("requires_human_approval", item.get("approval_required", False))
                    label = "Needs Approval" if approval else "Auto-Approved"
                    icon = "lock" if approval else "check"
                    with st.expander(f"{idx+1}. {item.get('action', item.get('recommendation', item.get('title', 'Step')))} — {label}"):
                        st.write(item.get("description", item.get("reason", "")))
                        impl = item.get("implementation", item.get("sql", item.get("command", "")))
                        if impl:
                            st.code(impl, language="sql")
                        regs = item.get("regulation", item.get("regulations_violated", []))
                        if regs:
                            if isinstance(regs, list):
                                st.caption(f"Regulations: {', '.join(regs)}")
                            else:
                                st.caption(f"Regulation: {regs}")
                elif isinstance(item, str):
                    st.markdown(f"{idx+1}. {item}")

        # Compliance mapping
        mapping = comp_data.get("compliance_mapping", [])
        if isinstance(mapping, list) and mapping:
            st.markdown("---")
            st.markdown("#### Compliance Mapping")
            for m in mapping:
                if isinstance(m, dict):
                    st.markdown(f"- **{m.get('regulation', m.get('framework', ''))}** — {m.get('description', m.get('requirement', m.get('article', '')))}")
                elif isinstance(m, str):
                    st.markdown(f"- {m}")

        with st.expander("Raw Compliance Output"):
            st.json(comp_data)
    else:
        st.info("Run a security scan first to see remediation recommendations.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# TAB 5: Alerts & Approvals
# ---------------------------------------------------------------------------
with tab_alerts:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### Security Alerts")

    col_filter, col_refresh = st.columns([2, 1])
    with col_filter:
        sev_filter = st.selectbox("Filter by severity", ["ALL", "CRITICAL", "HIGH", "MEDIUM", "LOW"])
    with col_refresh:
        st.markdown("<br>", unsafe_allow_html=True)
        refresh = st.button("Refresh Alerts")

    alerts_list = get_alerts(severity_filter=sev_filter if sev_filter != "ALL" else None)

    if alerts_list:
        for alert in alerts_list:
            sev = alert.get("severity", "MEDIUM").upper()
            sev_class = f"sev-{sev.lower()}"
            status = alert.get("status", "NEW")
            ts = alert.get("timestamp", "")
            try:
                ts_display = datetime.fromisoformat(ts).strftime("%Y-%m-%d %H:%M")
            except Exception:
                ts_display = ts

            status_color = {"NEW": "#EF4444", "ACKNOWLEDGED": "#F59E0B", "RESOLVED": "#10B981"}.get(status, "#6B7280")
            st.markdown(f"""
            <div class="metric-card {sev_class} risk-row" style="margin-bottom:0.8rem;">
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        {severity_badge(sev)}
                        <strong style="margin-left:8px;">{alert.get('risk_id', alert.get('id', '')[:8])}</strong>
                    </div>
                    <div>
                        <span class="badge" style="background:{status_color};">{status}</span>
                        <span style="font-size:0.8rem;color:#9CA3AF;margin-left:8px;">{ts_display}</span>
                    </div>
                </div>
                <p style="margin:0.5rem 0 0;color:#374151;">{alert.get('description', 'No description')}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No alerts found. Alerts appear here when CRITICAL or HIGH risks are published to Event Grid and processed by the Logic App.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# TAB 6: Scan History
# ---------------------------------------------------------------------------
with tab_history:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("### Scan History")

    history = get_scan_history(limit=20)
    if history:
        for idx, item in enumerate(history):
            ts = item.get("timestamp", "")
            try:
                ts_display = datetime.fromisoformat(ts).strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                ts_display = ts

            scan_type = item.get("scanType", "unknown").capitalize()
            datasets = item.get("datasets_scanned", [])
            score = item.get("compliance_score", "N/A")
            risk_sum = item.get("risk_summary", {})

            with st.expander(f"{ts_display} — {scan_type} Scan — Score: {score}"):
                st.caption(f"Datasets: {', '.join(datasets) if datasets else 'N/A'}")
                if risk_sum:
                    st.json(risk_sum)
                if item.get("classification"):
                    st.markdown("**Classification:**")
                    st.json(item["classification"])
                if item.get("risks"):
                    st.markdown("**Risks:**")
                    st.json(item["risks"])
                if item.get("compliance"):
                    st.markdown("**Compliance:**")
                    st.json(item["compliance"])

                if st.button(f"Load this scan", key=f"load_hist_{idx}"):
                    st.session_state["last_scan"] = item
                    st.rerun()
    else:
        st.info("No scan history yet. Run a security scan to see past results here.")

    st.markdown("</div>", unsafe_allow_html=True)
