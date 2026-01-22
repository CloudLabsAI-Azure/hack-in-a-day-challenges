# Feasibility Plan — Secure Production-style AI Lab (6‑hour hackathon)

## Purpose
This document outlines a pragmatic, timeboxed feasibility plan for a sandboxed hackathon lab where participants deploy a secure, isolated AI application (chat-based sample) inside per-team resource groups. The goal is a minimal, repeatable flow that proves the architecture (private networking, Key Vault, private endpoints, identity) is feasible within a 6‑hour hands-on window.

## Assumptions
- Organizer provides a shared Azure subscription and creates one dedicated RG per team prior to the event.
- ~300 teams expected (concurrency planning done separately). Resource quotas and limits will be handled by organizers.
- Participants perform all deployment steps inside their assigned RG.
- Manual validation by judges is acceptable for feasibility testing.
- No production hardening required — this is a lab-level feasibility test only.

## High-level architecture (minimal, feasible)
- Per-team resources in a single RG:
  - VNet with two subnets: `infra-subnet` (private endpoints, Key Vault) and `app-subnet` (Container Apps / App Service Environment / AKS).
  - Network Security Groups (NSGs) with restrictive inbound rules (deny Internet to private subnets).
  - Azure Key Vault (soft-delete enabled) for secrets and keys.
  - Azure AI Foundry / Azure OpenAI access (workspace or resource) with Private Endpoint(s) into `infra-subnet`.
  - Container App (or single-node AKS) hosting a sample chat app that uses Azure AI Foundry/OpenAI via private endpoint.
  - Private DNS zone(s) linked to VNet to resolve private endpoint hosts.
  - Bastion or JumpVM per organizer for participant access into the VNet for validation.

Notes: Container Apps with VNet integration is the fastest path for participants; AKS is more powerful but slower to provision and manage.

## Organizer (pre-event) — must-provision items
1. Create shared subscription, assign quotas, and enable required providers.
2. Create a pre-provisioned RG per team (naming convention e.g., `hack-<event>-team-###`).
3. Provide a JumpVM/Bastion host (or a pool of JumpVMs) in a management RG that can reach teams' VNets for manual validation.
4. Upload sample dataset and sample app repo links to the lab assets. Provide `README` with exact sample app steps.
5. Pre-create or share service principals or policies if you want participants to avoid interactive admin consent. (Optional.)
6. Provide a minimal Bicep/ARM/AZD template skeleton participants can optionally use to speed provisioning (not mandatory).

## Participant tasks (time estimates for 6‑hour window)
Total target: ~4.5–5 hours hands-on, leaving buffer for demo/cleanup.

1. (10–20m) Review lab README and clone sample app repo.
2. (20–40m) Create VNet and two subnets + NSG rules. Verify subnet delegation if required.
3. (10–15m) Deploy Key Vault into `infra-subnet` (or a separate secure RG if policy requires).
4. (15–30m) Deploy Azure AI Foundry workspace or configured Azure OpenAI resource and create Private Endpoint(s) into `infra-subnet`.
5. (10–20m) Add Private DNS zone and link to VNet; confirm DNS resolution for private endpoints.
6. (30–90m) Deploy sample chat app to Container Apps (or App Service in VNet / single-node AKS) with VNet integration and Managed Identity.
7. (10–20m) Configure Managed Identity for the app and grant it access to Key Vault secrets and AI resource roles.
8. (10–20m) Validate connectivity via Bastion/JumpVM: connect to Container App (via port-forward, curl) or test app from JumpVM.
9. (10–30m) Demo to judges and cleanup (delete non-essential resources if desired).

Alternative shortcut: If private endpoints prove slow, allow a timeboxed exception to use public endpoint + client-side API key stored in Key Vault — but mark as exception in grading.

## Minimal sample app behavior (recommendation)
- Chat UI (simple Flask/Streamlit) that sends user messages to AI Foundry/OpenAI with a short prompt and displays replies.
- Use Managed Identity to fetch API key/secret from Key Vault at runtime (or use Azure AD auth if supported by AI resource).
- Optionally include a basic RAG flow (upload a small sample doc set to Storage + use a simple similarity lookup) if time permits.

## Manual validation checklist (for judges)
- App reachable from Bastion/JumpVM and responds to queries.
- Private endpoints are present in `infra-subnet` and DNS resolves to private IPs.
- Key Vault access restricted to the app's Managed Identity; public Key Vault firewall is enabled (no public access).
- No public inbound rules allow Internet to app or infra subnets (unless exception granted).
- Resource tags and team RG naming follow convention.

## Recommended templates & assets to prepare (organizer)
- Small starter repo with: containerized chat app, `Dockerfile`, sample `requirements.txt`, and README with exact commands to deploy to Container Apps.
- Bicep/ARM/az CLI snippets to create VNet, Key Vault, Private Endpoint, Private DNS zone link, and Container App with VNet integration.
- Quick troubleshooting doc for private DNS issues and common Azure private endpoint delays.

## Time-risk mitigation for 6‑hour hackathon
- Provide a ready-to-clone starter repo + scripted deploy (az CLI / Bicep) to reduce time-to-first-success.
- Provide a fallback “public ingress” lab variant that teams can opt into if private endpoints fail during the event.
- Maintain a small ops team to help onboard teams with quota or DNS issues.

## Next steps (from me)
- I can convert these steps into a single-page lab guide `feasibility-plan.md` inside the lab folder (done), or generate the sample repo + Bicep snippets if you want test assets.
- Tell me which sample app you prefer: `simple-chat` or `chat-with-small-RAG` (RAG will need a small dataset and similarity index). Also tell me if you want Bicep templates or CLI snippets.

---

*File created as the feasibility blueprint for the lab.*
