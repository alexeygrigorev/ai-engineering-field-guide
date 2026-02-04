import re
from typing import Literal

AiType = Literal['ai-first', 'ai-support', 'unknown']


def get_ai_type(title: str) -> AiType:
    """
    Classify a job title into AI types.

    Args:
        title: Job title string

    Returns:
        'ai-first': Core AI/ML engineering roles (building models, research, AI infrastructure)
        'ai-support': Traditional SWE roles applied to AI products/teams
        'unknown': Non-AI roles or unclear classification
    """
    if not title or not isinstance(title, str):
        return 'unknown'

    t = title.lower().strip()

    # ===== AI-FIRST PATTERNS =====
    # Core AI roles - building/deploying AI models is the primary work
    ai_first_patterns = [
        r'\bfull stack ai engineer\b',
        r'\bfullstack ai engineer\b',
        r'\bai engineer\b(?!.*\bsoftware\b)',
        r'\bai / ml engineer\b',
        r'\bai & ml engineer\b',
        r'\bai/ml engineer\b',
        r'\bml engineer\b',
        r'\bmachine learning engineer\b',
        r'\bapplied ai engineer\b',
        r'\bgenerative ai engineer\b',
        r'\bgen ai engineer\b',
        r'\bai research engineer\b',
        r'\bai researcher\b',
        r'\bai scientist\b',
        r'\bapplied scientist\b',
        r'\bconversational ai engineer\b',
        r'\bcomputer vision ai engineer\b',
        r'\bdistinguished ai engineer\b',
        r'\bprincipal ai engineer\b',
        r'\bfounding ai engineer\b',
        r'\bai deployment engineer\b',
        r'\bai inference engineer\b',
        r'\bai prompt engineer\b',
        r'\bai safety engineer\b',
        r'\bartificial intelligence engineer\b',
        r'\bagentic artificial intelligence\b',
        r'\bml ops engineer\b',
        r'\bmlops engineer\b',
        r'\bai developer\b(?!.*\bsoftware\b)',
        r'\bai developer technology engineer\b',
        r'\bai developer tooling engineer\b',
        r'\bai native engineer\b',
        r'\bai principal engineer\b',
        r'\bai product & research engineer\b',
        r'\bartificial intelligence software engineer sme\b',
        r'\bdistinguished engineer.*ai\b',
        r'\blead research engineer.*ai\b',
        r'\blead engineer, ai platform\b',
        r'\bmanaging engineer.*ai\b',
        r'\bprincipal ai developer\b',
        r'\bprincipal conversational ai\b',
        r'\bprincipal engineer - voice ai\b',
        r'\bprincipal engineer, ai systems\b',
        r'\bprincipal engineer, generative & agentic ai\b',
        r'\bresearch engineer - decentralized ai\b',
        r'\bresearch engineer, ai\b',
        r'\bresearch scientist/research engineer, ai\b',
        r'\bsenior ai developer\b',
        r'\bsenior ai tools engineer\b',
        r'\bsenior ai/ml developer\b',
        r'\bsenior context engineer, ai systems\b',
        r'\bsenior engineer applied ai\b',
        r'\bsenior hpc and ai\b',
        r'\bsenior machine learning \(ml\) engineer\b',
        r'\bsenior math libraries engineer.*ai\b',
        r'\bsenior principal research engineer.*generative ai\b',
        r'\bsenior staff ai application engineer\b',
        r'\bsenior systems engineer, ai applications\b',
        r'\bsenior/principal systems engineer.*ai\b',
        r'\bsr ai/hpc\b',
        r'\bsr\. ai application developer\b',
        r'\bsr\. ai systems engineer\b',
        r'\bstaff ai api engineer\b',
        r'\bstaff ai innovation engineer\b',
        r'\bstaff ai ops engineer\b',
        r'\bstaff ai systems engineer\b',
        r'\bstaff level research engineer, ai\b',
        r'\blead engineer \(ai and agent development\)\b',
    ]

    for pattern in ai_first_patterns:
        if re.search(pattern, t):
            return 'ai-first'

    # ===== AI-SUPPORT PATTERNS =====
    # Traditional SWE roles applied to AI context
    ai_support_patterns = [
        r'\bsoftware engineer.*\bai\b',
        r'\bsoftware engineer, ai\b',
        r'\bsoftware engineer \(ai\)',
        r'\bsoftware engineer - ai\b',
        r'\bai software engineer\b',
        r'\bsoftware developer.*\bai\b',
        # Full stack with AI but NOT "Full Stack AI Engineer"
        r'\bfull stack engineer.*\b\(ai\)',
        r'\bfull stack engineer.*\bai team\b',
        r'\bfullstack engineer.*\b\(ai\)',
        r'\bfull-stack engineer.*\bai\b',
        r'\bbackend engineer.*\bai\b',
        r'\bback-end engineer.*\bai\b',
        r'\bfrontend engineer.*\bai\b',
        r'\bfront-end engineer.*\bai\b',
        r'\bdata engineer.*\bai\b',
        r'\bsite reliability engineer.*\bai\b',
        r'\bdevops engineer.*\bai\b',
        r'\binfrastructure engineer.*\bai\b',
        r'\bplatform engineer.*\bai\b',
        r'\bsolutions engineer.*\bai\b',
        r'\bsales engineer.*\bai\b',
        r'\bintegration engineer.*\bai\b',
        r'\bqa engineer.*\bai\b',
        r'\btest engineer.*\bai\b',
        r'\bproduct engineer.*\bai\b(?!.*\bresearch)',
        r'\bautomation engineer.*\bai\b(?!.*\bai\b)',
        r'\bandroid developer.*\bai\b',
        r'\bios developer.*\bai\b',
        r'\bsecurity engineer.*\bai\b',
        r'\bappsec engineer.*\bai\b',
        r'\benablement engineer\b',
        r'\bintegrations engineer\b',
        r'\bapplications engineer\b',
        r'\bproduct developer\b',
        r'\bsolution engineer\b',
        r'\bcustomer engineer\b',
        r'\bsuccess engineer\b',
        r'\bforward deployed engineer.*\bai\b',
        r'\bdeveloper relations',
        r'\bdesign engineer.*\bai\b',
        r'\bgtm engineer.*\bai\b',
        r'\bworkplace engineer.*\bai\b',
        r'\bquantitative developer.*\bai\b',
        r'\bsimulation engineer.*\bai\b',
        r'\bsupport engineer.*\bai\b',
        r'\btechnical operations.*\bai\b',
        r'\bdeveloper.*\bapprentice',
        r'\bai account engineer\b',
        r'\bai application engineer\b',
        r'\bai automation engineer\b',
        r'\bai operations engineer\b',
        r'\bai ops engineer\b',
        r'\bai process automation engineer\b',
        r'\bai software developer\b',
        r'\blead engineer.*business intelligence',
        r'\blead identity engineer.*ai\b',
        r'\bontology engineer\b',
        r'\bprincipal ai & data platforms engineer\b',
        r'\bsenior ai integration engineer\b',
        r'\bsenior azure cloud.*ai\b',
        r'\bsenior backend application engineer - ai\b',
        r'\bsenior engineer.*interactive voice response.*ai\b',
        r'\bsenior front-end engineer.*ai\b',
        r'\bsenior full-stack engineer.*physical ai\b',
        r'\bsenior gen ai developer\b',
        r'\bit engineer.*ai\b',
        r'\bjava engineer - ai enablement\b',
        r'\bknowledge graph engineer.*ai\b',
        r'\bmanager, solutions architecture.*ai\b',
        r'\bpython engineer - ai\b',
        r'\bsenior specialist.*ai\b',
        r'\bsenior technical writer.*ai\b',
        r'\bsr application engineer.*ai\b',
        r'\bsr data governance engineer.*ai\b',
        r'\bsr\. full-stack engineer.*applied ai\b',
        r'\bsr\. software reliability engineer for ai\b',
        r'\bstaff product designer.*ai\b',
        r'\btrading ops.*ai\b',
        # Additional patterns from unknown list
        r'\bai forward deployed engineer\b',
        r'\bai operations automation engineer\b',
        r'\bclojure.*engineer.*ai\b',
        r'\bcontract principal.*automation.*ai\b',
        r'\bdata solutions.*ai application developer\b',
        r'\bflowfuse.*developer.*ai\b',
        r'\bfounding engineer.*ai\b',
        r'\bfull stack \+ ai engineer\b',
        r'\bfull stack developer.*ai model experience\b',
        r'\blead ai appsec engineer\b',
        r'\blead engineer \(ai and agent development\)',
        r'\bprincipal engineer - ai and intelligence systems\b',
        r'\bsenior \.net engineer.*ai\b',
        r'\bsenior associate.*ai solutions\b',
        r'\bsenior developer.*ai\b',
        r'\bsenior engineer- applied ai\b',
        r'\bsenior software engineer- artificial intelligence\b',
        r'\bsenior software engineer-.*artificial intelligence\b',
    ]

    for pattern in ai_support_patterns:
        if re.search(pattern, t):
            return 'ai-support'

    # ===== KEYWORD FALLBACKS =====

    # Check for clear AI-first keywords
    ai_first_keywords = [
        'machine learning engineer',
        'ml engineer',
        'applied ai engineer',
        'generative ai engineer',
        'ai research engineer',
        'ai scientist',
        'applied scientist',
        'ai deployment engineer',
        'ai inference engineer',
        'ai prompt engineer',
        'ai safety engineer',
    ]

    for kw in ai_first_keywords:
        if kw in t and 'software engineer' not in t:
            return 'ai-first'

    # Check for AI-support keywords (SWE + AI context)
    ai_support_phrases = [
        'software engineer',
        'full stack engineer',
        'fullstack engineer',
        'backend engineer',
        'frontend engineer',
        'data engineer',
        'site reliability',
        'devops',
        'infrastructure engineer',
        'platform engineer',
        'solutions engineer',
        'sales engineer',
        'product engineer',
        'staff engineer',
    ]

    for phrase in ai_support_phrases:
        if phrase in t and 'ai' in t:
            return 'ai-support'

    # ===== FINAL CHECK =====
    # Has AI keyword but unclear role
    ai_keywords = ['ai', 'machine learning', 'ml', 'llm', 'gen ai', 'generative ai', 'agentic ai']
    has_ai = any(kw in t for kw in ai_keywords)

    if not has_ai:
        return 'unknown'

    return 'unknown'


# Usage example
if __name__ == '__main__':
    test_titles = [
        "AI Engineer",
        "Senior AI Engineer",
        "Software Engineer, AI (Python)",
        "Full Stack Engineer (AI)",
        "Backend Engineer (AI Agents)",
        "Machine Learning Engineer",
        "AI Research Engineer",
        "Senior Software Engineer (AI Platform)",
        "Frontend Developer",
        "Product Manager",
    ]

    print("AI Type Classification Examples:")
    print("-" * 50)
    for title in test_titles:
        ai_type = get_ai_type(title)
        print(f"{title:50} -> {ai_type}")
