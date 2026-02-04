import pandas as pd
import re

# AI-First patterns - roles where building AI models/systems is the core focus
AI_FIRST_PATTERNS = [
    r'\bAI Engineer\b(?!\s*\(?\w*Software)',  # AI Engineer but not "AI Software Engineer"
    r'\bAI/ML Engineer\b',
    r'\bAI & ML Engineer\b',
    r'\bAI / Machine Learning Engineer\b',
    r'\bAI / ML Engineer\b',
    r'\bAI & ML\b',
    r'\bML Engineer\b',
    r'\bMachine Learning Engineer\b',
    r'\bApplied AI Engineer\b',
    r'\bApplied AI / Machine Learning Engineer\b',
    r'\bApplied AI/ML Engineer\b',
    r'\bGenerative AI Engineer\b',
    r'\bGen AI Engineer\b',
    r'\bGenerative AI / Machine Learning Engineer\b',
    r'\bAI Research Engineer\b',
    r'\bAI Scientist\b',
    r'\bResearch Scientist/Research Engineer\b',
    r'\bAI Developer\b(?!\s+\(.*Software)',  # AI Developer but not in a software context
    r'\bAI Application Engineer\b',
    r'\bAI Automation Engineer\b',
    r'\bAI Infrastructure Engineer\b',
    r'\bAI Platform Engineer\b',
    r'\bAI Ops Engineer\b',
    r'\bAI Operations Engineer\b',
    r'\bConversational AI Engineer\b',
    r'\bComputer Vision AI Engineer\b',
    r'\bAI Native Engineer\b',
    r'\bAI Native Software Engineer\b',
    r'\bDistinguished AI Engineer\b',
    r'\bPrincipal AI Engineer\b',
    r'\bAI Principal Engineer\b',
    r'\bAI Data Engineer\b',
    r'\bGen AI Data Engineer\b',
    r'\bFounding AI Engineer\b',
    r'\bStaff AI Engineer\b',
    r'\bSenior AI Engineer\b',
    r'\bLead AI Engineer\b',
    r'\bJunior AI Engineer\b',
    r'\bAI Engineer II\b',
    r'\bAI Engineer 2\b',
    r'\bAI Engineer I\b',
    r'\bFull Stack AI Engineer\b',
    r'\bFullstack AI Engineer\b',
    r'\bAI/ML Full Stack Engineer\b',
    r'\bSenior AI Full-Stack Software Engineer\b',
    r'\bSenior Full-Stack AI Engineer\b',
    r'\bAI & Researcher\b',
    r'\bAI Product & Research Engineer\b',
    r'\bAI Research Engineer - AI Safety\b',
    r'\bAI Research Engineer - Reinforcement Learning\b',
    r'\bAI Research Engineer - Signal Processing\b',
    r'\bAI Research Engineer - Robotics\b',
    r'\bAI/ML Engineer\b',
    r'\bAI ML Engineer\b',
    r'\bAgentic AI\b.*\bEngineer\b',
    r'\bEntrepreneurial AI Research Engineer\b',
    r'\bML/AI Engineer\b',
]

# AI-Support patterns - traditional SWE roles applied to AI products
AI_SUPPORT_PATTERNS = [
    r'\bSoftware Engineer.*\bAI\b',
    r'\bSoftware Engineer, AI\b',
    r'\bSoftware Engineer \(AI\)',
    r'\bSoftware Engineer - AI\b',
    r'\bSoftware Engineer – AI\b',
    r'\bSenior Software Engineer.*AI\b',
    r'\bStaff Software Engineer.*AI\b',
    r'\bPrincipal Software Engineer.*AI\b',
    r'\bLead Software Engineer.*AI\b',
    r'\bFull Stack Engineer.*\bAI\b(?!\s*Engineer)',  # Full Stack Engineer (AI) but not Full Stack AI Engineer
    r'\bFullstack Engineer.*\bAI\b',
    r'\bFull-Stack Engineer.*\bAI\b',
    r'\bBackend Engineer.*\bAI\b',
    r'\bBack-End Engineer.*\bAI\b',
    r'\bFrontend Engineer.*\bAI\b',
    r'\bFront-End Engineer.*\bAI\b',
    r'\bData Engineer.*\bAI\b',
    r'\bData Engineer.*\bML\b',
    r'\bSenior Data Engineer.*\bAI\b',
    r'\bSite Reliability Engineer.*\bAI\b',
    r'\bSenior Site Reliability Engineer.*\bAI\b',
    r'\bDevOps Engineer.*\bAI\b',
    r'\bSenior DevOps Engineer.*\bAI\b',
    r'\bMLOps Engineer\b',
    r'\bAI/ML Ops Engineer\b',
    r'\bSenior AI/ML Ops Engineer\b',
    r'\bProduct Engineer.*\bAI\b',
    r'\bSenior Product Engineer.*\bAI\b',
    r'\bStaff Product Engineer.*\bAI\b',
    r'\bInfrastructure Engineer.*\bAI\b',
    r'\bSenior Infrastructure Engineer.*\bAI\b',
    r'\bPlatform Engineer.*\bAI\b',
    r'\bPlatform Engineer.*\bML\b',
    r'\bSolutions Engineer.*\bAI\b',
    r'\bAI Solutions Engineer\b',
    r'\bSenior AI Solutions Engineer\b',
    r'\bSales Engineer.*\bAI\b',
    r'\bAI Sales Engineer\b',
    r'\bIntegration Engineer.*\bAI\b',
    r'\bQA Engineer.*\bAI\b',
    r'\bQA Automation Engineer.*\bAI\b',
    r'\bTest Engineer.*\bAI\b',
    r'\bAutomation Engineer.*\bAI\b',
    r'\bAI Success Engineer\b',
    r'\bCustomer AI Engineer\b',
    r'\bAI Account Engineer\b',
    r'\bForward Deployed Engineer.*\bAI\b',
    r'\bAI Forward Deployed Engineer\b',
    r'\bAI Software Engineer\b',
    r'\bAI Software Engineer \(',
    r'\bAI Staff Software Engineer\b',
    r'\bStaff Software Engineer.*\bAI\b',
    r'\bSenior/Staff.*\bEngineer.*\bAI\b',
    r'\bStaff.*\bEngineer.*\bAI\b',
    r'\bSenior.*\bEngineer.*\bAI\b',
    r'\bLead.*\bEngineer.*\bAI\b',
    r'\bPrincipal.*\bEngineer.*\bAI\b',
    r'\bStaff Fullstack Engineer.*\bAI\b',
    r'\bStaff Full-Stack Engineer.*\bAI\b',
    r'\bSenior Full Stack Engineer.*\bAI\b',
    r'\bSenior Full-Stack Engineer.*\bAI\b',
    r'\bSenior/Staff Full Stack Engineer.*\bAI\b',
    r'\bLead Full Stack Engineer.*\bAI\b',
    r'\bPrincipal Full Stack Engineer.*\bAI\b',
    r'\bStaff Backend Engineer.*\bAI\b',
    r'\bSenior Backend Engineer.*\bAI\b',
    r'\bLead Backend Engineer.*\bAI\b',
    r'\bStaff Frontend Engineer.*\bAI\b',
    r'\bSenior Frontend Engineer.*\bAI\b',
    r'\bLead Frontend Engineer.*\bAI\b',
    r'\bStaff Systems Engineer.*\bAI\b',
    r'\bSenior Systems Engineer.*\bAI\b',
    r'\bAI-Enabled Software Engineer\b',
    r'\bAI - Enabled Software Engineer\b',
    r'\bFlowFuse Full Stack Developer \(AI-focused\)',
    r'\bFounding Engineer.*\bAI\b',
    r'\bFounding AI Product Engineer\b',
    r'\bFounding AI/Data Engineer\b',
    r'\bFounding Staff AI Engineer\b',
    r'\bFull Stack Engineer \(AI\)',
    r'\bFull Stack Engineer \(Libra',
    r'\bFull Stack Software Engineer.*\bAI\b',
    r'\bFullstack Engineer, Generative AI\b',
    r'\bSenior MLOps Engineer\b',
    r'\bIT Engineer \(AI\b',
    r'\bJava Engineer - AI Enablement\b',
    r'\bPython Engineer - AI\b',
    r'\bKnowledge Graph Engineer / AI Architect\b',
    r'\bSenior Staff.*\bEngineer.*\bAI\b',
    r'\bSr\.\b.*\bEngineer.*\bAI\b',
    r'\bSr\b.*\bEngineer.*\bAI\b',
]

# Non-AI patterns - roles that are not AI-related
NON_AI_PATTERNS = [
    r'\bAndroid Developer\b',
    r'\biOS Developer\b',
    r'\bSales Engineer\b(?!\s*.*\bAI\b)',
    r'\bSolutions Engineer\b(?!\s*.*\bAI\b)',
    r'\bGTM Engineer\b',
    r'\bProduct Manager\b',
    r'\bVice President\b',
    r'\bManager\b',
    r'\bDirector\b',
    r'\bQA Engineer\b(?!\s*.*\bAI\b)',
    r'\bDevOps Engineer\b(?!\s*.*\bAI\b)',
    r'\bSite Reliability Engineer\b(?!\s*.*\bAI\b)',
]

def classify_job(title: str) -> str:
    """
    Classify a job title into one of three categories:
    - 'ai_first': Core AI/ML engineering roles
    - 'ai_support': Traditional SWE roles applied to AI products
    - 'other': Non-AI roles or unclear
    """
    title_lower = title.lower()

    # Additional AI-First patterns from manual review
    additional_ai_first = [
        'deployment engineer',
        'inference engineer',
        'prompt engineer',
        'agentic artificial intelligence',
        'artificial intelligence engineer',
        'ai scientist',
        'ai researcher',
        'ai safety engineer',
        'ai systems engineer',
        'ai api engineer',
        'ai application developer',
        'ai/ml developer',
        'ai tools engineer',
        'ai innovation engineer',
        'distinguished engineer.*ai',
        'managing engineer.*ai',
        'vice president.*ai.*engineer',
    ]

    # Additional AI-Support patterns from manual review
    additional_ai_support = [
        'applications engineer',
        'enablement engineer',
        'integrations engineer',
        'product developer',
        'solution engineer',
        'staff engineer.*ai',
        'android developer.*ai',
        'ios developer.*ai',
        'clojure.*ai',
        'consulting.*engineer.*ai',
        'developer relations',
        'apprenticeship',
        'design engineer.*ai',
        'gtm engineer.*ai',
        'workplace engineer.*ai',
        'appsec engineer.*ai',
        'manager.*solutions',
        'customer engineer',
        'quantitative developer.*ai',
        'simulation engineer.*ai',
        'support engineer.*ai',
        'technical operations.*ai',
        'trading.*ai',
        'solutions architecture',
    ]

    # AI-Support specific phrases (SWE applied to AI)
    ai_support_phrases = [
        'full stack engineer',
        'fullstack engineer',
        'backend engineer',
        'frontend engineer',
        'software engineer',
        'data engineer',
        'site reliability',
        'devops',
        'infrastructure engineer',
        'platform engineer',
        'solutions engineer',
        'sales engineer',
        'integration engineer',
        'qa engineer',
        'automation engineer',
        'test engineer',
        'product engineer',
        'staff engineer',
    ]

    # Check AI-First patterns first (more specific)
    for pattern in AI_FIRST_PATTERNS + additional_ai_first:
        if re.search(pattern, title, re.IGNORECASE):
            # Make sure it's not actually an AI-support pattern
            is_support = False
            for phrase in ai_support_phrases:
                if phrase in title_lower:
                    # Check if the SWE role comes before AI (suggesting SWE applied to AI)
                    # e.g., "Software Engineer, AI" vs "AI Engineer"
                    title_words = title_lower.split()
                    for i, word in enumerate(title_words):
                        if 'ai' in word and i > 0:
                            # Check if previous words indicate SWE role
                            prev_phrase = ' '.join(title_words[max(0, i-3):i])
                            if any(p in prev_phrase for p in ['software', 'full stack', 'fullstack', 'backend', 'frontend', 'data', 'staff']):
                                is_support = True
                                break
                    if is_support:
                        break
            if not is_support:
                return 'ai_first'

    # Check AI-Support patterns
    for pattern in AI_SUPPORT_PATTERNS + additional_ai_support:
        if re.search(pattern, title, re.IGNORECASE):
            return 'ai_support'

    # Check for specific AI-first keywords
    ai_first_keywords = [
        'machine learning engineer',
        'ml engineer',
        'applied ai engineer',
        'generative ai engineer',
        'gen ai engineer',
        'ai research engineer',
        'conversational ai engineer',
        'computer vision ai engineer',
        'ai infrastructure engineer',
        'ai platform engineer',
        'ai ops engineer',
        'distinguished ai engineer',
        'principal ai engineer',
        'founding ai engineer',
        'ai deployment engineer',
        'ai inference engineer',
        'ai prompt engineer',
        'ai safety engineer',
        'artificial intelligence engineer',
    ]

    for keyword in ai_first_keywords:
        if keyword in title_lower:
            # Double-check it's not actually software engineering
            if not any(p in title_lower for p in ['software engineer', 'full stack', 'fullstack', 'backend engineer', 'frontend engineer']):
                return 'ai_first'

    # Check for AI-support keywords (SWE roles with AI context)
    for phrase in ai_support_phrases:
        if phrase in title_lower and 'ai' in title_lower:
            return 'ai_support'

    # Check if it has AI at all - if not, it's other
    ai_keywords = ['ai', 'machine learning', 'ml', 'gen ai', 'generative ai', 'llm', 'agentic ai']
    has_ai = any(kw in title_lower for kw in ai_keywords)

    if not has_ai:
        return 'other'

    # Default to other for unclear cases
    return 'other'


def main():
    # Load the data
    df = pd.read_csv('jobs/all_jobs_dedup.csv')

    # Apply classification
    df['classification'] = df['title'].apply(classify_job)

    # Print summary
    print("=" * 60)
    print("JOB CLASSIFICATION SUMMARY")
    print("=" * 60)
    print(f"\nTotal jobs: {len(df)}")
    print(f"\nAI-First (core AI/ML roles): {len(df[df['classification'] == 'ai_first'])}")
    print(f"AI-Support (SWE roles in AI teams): {len(df[df['classification'] == 'ai_support'])}")
    print(f"Other: {len(df[df['classification'] == 'other'])}")

    # Print sample titles for each category
    print("\n" + "=" * 60)
    print("AI-FIRST ROLES (sample)")
    print("=" * 60)
    ai_first = df[df['classification'] == 'ai_first']['title'].unique()
    for title in sorted(ai_first)[:30]:
        print(f"  {title}")

    print("\n" + "=" * 60)
    print("AI-SUPPORT ROLES (sample)")
    print("=" * 60)
    ai_support = df[df['classification'] == 'ai_support']['title'].unique()
    for title in sorted(ai_support)[:30]:
        print(f"  {title}")

    print("\n" + "=" * 60)
    print("OTHER ROLES (sample)")
    print("=" * 60)
    other = df[df['classification'] == 'other']['title'].unique()
    for title in sorted(other)[:20]:
        print(f"  {title}")

    # Save classified data
    df.to_csv('jobs/all_jobs_classified.csv', index=False)
    print(f"\nClassified data saved to jobs/all_jobs_classified.csv")


if __name__ == '__main__':
    main()
