#!/usr/bin/env python3
"""
CRESTLINE Marketing Psychology Tool
====================================
A comprehensive tool for brand name analysis, audience psychology profiling,
and marketing script generation based on behavioral psychology frameworks.

Author: Marketing Strategy AI
Date: 2025-11-10
"""

import json
import re
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
from enum import Enum


class AudienceSegment(Enum):
    """Target audience segments with age ranges"""
    GEN_ALPHA_YOUNG = "Gen Alpha Young (10-13)"
    GEN_ALPHA_OLD = "Gen Alpha Old (14-17)"
    PARENT_BUYERS = "Parent Buyers (30-45)"
    GEN_Z_YOUNG = "Gen Z Young (18-23)"
    GEN_Z_OLD = "Gen Z Old (24-28)"
    MILLENNIAL_YOUNG = "Millennial Young (29-34)"
    MILLENNIAL_CORE = "Millennial Core (35-40)"
    GEN_X = "Gen X (41-56)"


class Platform(Enum):
    """Social media platforms for script generation"""
    TIKTOK = "TikTok"
    INSTAGRAM_REELS = "Instagram Reels"
    YOUTUBE_SHORTS = "YouTube Shorts"
    INSTAGRAM_POST = "Instagram Post"
    TWITTER = "Twitter/X"
    EMAIL = "Email Marketing"


class PsychologyFramework(Enum):
    """Psychology frameworks for analysis"""
    CIALDINI = "Cialdini's 6 Principles"
    SELF_DETERMINATION = "Self-Determination Theory"
    GAMIFICATION = "Gamification (Octalysis)"
    IDENTITY = "Identity Theory"
    FOGG = "Fogg Behavior Model"


@dataclass
class PhoneticAnalysis:
    """Phonetic psychology analysis of a name"""
    initial_consonant: str
    syllable_count: int
    hard_consonants: List[str]
    vowel_sounds: List[str]
    rhythm_pattern: str
    memorability_score: float  # 0-10
    pronunciation_ease: float  # 0-10
    global_friendliness: float  # 0-10

    def overall_score(self) -> float:
        """Calculate overall phonetic score"""
        return (self.memorability_score + self.pronunciation_ease +
                self.global_friendliness) / 3


@dataclass
class BrandNameScore:
    """Comprehensive brand name scoring"""
    name: str
    phonetic_score: float
    emotional_valence: float  # -10 to +10
    uniqueness_score: float  # 0-10
    trademark_risk: str  # LOW, MEDIUM, HIGH
    seo_potential: float  # 0-10
    social_shareability: float  # 0-10
    generational_appeal: Dict[str, float]  # Segment -> score
    category_fit: float  # 0-10
    expandability: float  # 0-10
    overall_score: float

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AudiencePersona:
    """Psychological profile of target audience"""
    segment: AudienceSegment
    core_motivations: List[str]
    pain_points: List[str]
    aspirations: List[str]
    media_consumption: List[str]
    purchase_triggers: List[str]
    emotional_drivers: List[str]
    brand_values: List[str]
    nostalgia_references: List[str]
    skepticism_level: str  # LOW, MEDIUM, HIGH
    brand_loyalty: str  # LOW, MEDIUM, HIGH


class MarketingPsychologyTool:
    """Main marketing psychology analysis tool"""

    def __init__(self):
        self.audience_personas = self._initialize_personas()
        self.psychology_frameworks = self._initialize_frameworks()

    def _initialize_personas(self) -> Dict[AudienceSegment, AudiencePersona]:
        """Initialize audience persona database based on research"""
        return {
            AudienceSegment.GEN_Z_YOUNG: AudiencePersona(
                segment=AudienceSegment.GEN_Z_YOUNG,
                core_motivations=[
                    "Mental health & self-care",
                    "Authenticity & real connections",
                    "Social proof & community",
                    "Personal growth & skill development",
                    "Creative expression"
                ],
                pain_points=[
                    "Traditional golf feels exclusive/pretentious",
                    "High barrier to entry (cost, skill, time)",
                    "Lack of relatable content/culture",
                    "Not enough social/competitive elements",
                    "Boring, slow-paced perception"
                ],
                aspirations=[
                    "Be part of a cool, inclusive community",
                    "Master a skill that's unique/impressive",
                    "Create shareable content moments",
                    "Build online presence through hobby",
                    "Find mindful, meditative activities"
                ],
                media_consumption=[
                    "TikTok (primary discovery)",
                    "Instagram Reels",
                    "YouTube (how-to & entertainment)",
                    "Discord communities",
                    "Twitch streams"
                ],
                purchase_triggers=[
                    "Viral trends & influencer endorsement",
                    "Limited editions & scarcity",
                    "Community challenges & participation",
                    "Visual aesthetics (Instagrammable)",
                    "Interactive/gamified experiences"
                ],
                emotional_drivers=[
                    "FOMO (fear of missing out)",
                    "Belonging to in-group",
                    "Achievement & progression",
                    "Self-expression & identity",
                    "Curiosity & discovery"
                ],
                brand_values=[
                    "Authenticity (no fake corporate speak)",
                    "Inclusivity & accessibility",
                    "Environmental consciousness",
                    "Social responsibility",
                    "Transparency"
                ],
                nostalgia_references=[
                    "Pokémon (primary)",
                    "Naruto",
                    "Avatar: The Last Airbender",
                    "Early YouTube (2010s)",
                    "Minecraft"
                ],
                skepticism_level="HIGH",
                brand_loyalty="LOW"
            ),

            AudienceSegment.GEN_Z_OLD: AudiencePersona(
                segment=AudienceSegment.GEN_Z_OLD,
                core_motivations=[
                    "Career development & networking",
                    "Wellness & stress relief",
                    "Building real-world skills",
                    "Quality over quantity",
                    "Financial independence"
                ],
                pain_points=[
                    "Golf is expensive to start",
                    "Time commitment conflicts with career",
                    "Intimidating for beginners",
                    "Lack of peer participation",
                    "Old-school culture doesn't resonate"
                ],
                aspirations=[
                    "Join a hobby that aids networking",
                    "Develop a lifelong skill",
                    "Balance work with meaningful leisure",
                    "Be part of modern golf culture",
                    "Collect meaningful items with value"
                ],
                media_consumption=[
                    "Instagram (career & lifestyle)",
                    "LinkedIn (professional)",
                    "YouTube (in-depth content)",
                    "Podcasts",
                    "Reddit communities"
                ],
                purchase_triggers=[
                    "Peer recommendations",
                    "Quality & craftsmanship",
                    "Investment value",
                    "Practical utility + aesthetics",
                    "Brand story & mission"
                ],
                emotional_drivers=[
                    "Achievement & competence",
                    "Status & recognition",
                    "Personal growth",
                    "Connection & community",
                    "Control & autonomy"
                ],
                brand_values=[
                    "Authenticity & honesty",
                    "Quality & durability",
                    "Innovation",
                    "Social impact",
                    "Inclusivity"
                ],
                nostalgia_references=[
                    "Pokémon (childhood)",
                    "Naruto/Dragon Ball Z",
                    "Harry Potter",
                    "Early social media (Vine, early Instagram)",
                    "Classic Nintendo games"
                ],
                skepticism_level="HIGH",
                brand_loyalty="MEDIUM"
            ),

            AudienceSegment.MILLENNIAL_YOUNG: AudiencePersona(
                segment=AudienceSegment.MILLENNIAL_YOUNG,
                core_motivations=[
                    "Work-life balance",
                    "Experiences over things (but collectibles bridge both)",
                    "Nostalgia for childhood",
                    "Mastery & expertise",
                    "Social connection"
                ],
                pain_points=[
                    "Limited free time",
                    "Balancing family/career/hobbies",
                    "Want quality, not quantity",
                    "Tired of overhyped products",
                    "Seeking authenticity in brands"
                ],
                aspirations=[
                    "Master a skill worth investing in",
                    "Build a meaningful collection",
                    "Connect with like-minded people",
                    "Relive childhood joys with adult quality",
                    "Find hobbies that reduce stress"
                ],
                media_consumption=[
                    "Instagram (lifestyle)",
                    "Facebook groups (communities)",
                    "YouTube (long-form)",
                    "Podcasts",
                    "Email newsletters"
                ],
                purchase_triggers=[
                    "Nostalgia & emotional connection",
                    "Premium quality",
                    "Limited editions",
                    "Detailed reviews & research",
                    "Brand heritage & story"
                ],
                emotional_drivers=[
                    "Nostalgia",
                    "Achievement",
                    "Belonging",
                    "Status (subtle)",
                    "Competence"
                ],
                brand_values=[
                    "Quality & craftsmanship",
                    "Authenticity",
                    "Sustainability",
                    "Heritage & story",
                    "Community"
                ],
                nostalgia_references=[
                    "Transformers (original)",
                    "Pokémon (Red/Blue era)",
                    "Dragon Ball Z",
                    "Yu-Gi-Oh",
                    "90s culture"
                ],
                skepticism_level="MEDIUM",
                brand_loyalty="MEDIUM"
            ),

            AudienceSegment.MILLENNIAL_CORE: AudiencePersona(
                segment=AudienceSegment.MILLENNIAL_CORE,
                core_motivations=[
                    "Established hobbies & interests",
                    "Premium quality products",
                    "Networking & social status",
                    "Investment mindset",
                    "Legacy & tradition"
                ],
                pain_points=[
                    "Oversaturated market",
                    "Want established brands with heritage",
                    "Skeptical of new trends",
                    "Time-poor, money-rich",
                    "Want immediate quality signals"
                ],
                aspirations=[
                    "Be an early adopter of quality brands",
                    "Build valuable collections",
                    "Share passion with family/kids",
                    "Support brands that align with values",
                    "Achieve mastery in hobbies"
                ],
                media_consumption=[
                    "Facebook",
                    "LinkedIn",
                    "Email",
                    "Traditional media (TV, magazines)",
                    "Podcasts"
                ],
                purchase_triggers=[
                    "Brand reputation",
                    "Quality materials & craftsmanship",
                    "Investment potential",
                    "Expert endorsements",
                    "Heritage & authenticity"
                ],
                emotional_drivers=[
                    "Status & achievement",
                    "Nostalgia",
                    "Legacy",
                    "Competence",
                    "Autonomy"
                ],
                brand_values=[
                    "Heritage & tradition",
                    "Quality above all",
                    "Exclusivity (tasteful)",
                    "Sustainability",
                    "Craftsmanship"
                ],
                nostalgia_references=[
                    "80s/90s culture",
                    "Original Transformers",
                    "Classic sports memorabilia",
                    "Vintage collectibles",
                    "Traditional golf culture"
                ],
                skepticism_level="HIGH",
                brand_loyalty="HIGH"
            ),

            AudienceSegment.GEN_ALPHA_YOUNG: AudiencePersona(
                segment=AudienceSegment.GEN_ALPHA_YOUNG,
                core_motivations=[
                    "Fun & entertainment",
                    "Peer acceptance & fitting in",
                    "Collecting & completing sets",
                    "Gaming & interactive experiences",
                    "Learning new skills (when disguised as fun)"
                ],
                pain_points=[
                    "Golf seems boring/slow compared to video games",
                    "Need parental approval/money for purchases",
                    "Want instant gratification",
                    "Peer pressure (need friends who also play)",
                    "Short attention span"
                ],
                aspirations=[
                    "Be good at something their friends aren't",
                    "Have the coolest collectibles",
                    "Beat their parents/older siblings at something",
                    "Build impressive collections to show off",
                    "Be part of exclusive groups/clubs"
                ],
                media_consumption=[
                    "YouTube (primary - gaming, unboxing, tutorials)",
                    "TikTok (entertainment)",
                    "Roblox/Minecraft (gaming)",
                    "Instagram (following friends)",
                    "Twitch (watching gaming)"
                ],
                purchase_triggers=[
                    "Friend has it (peer influence #1)",
                    "YouTuber/influencer unboxing",
                    "Birthday/holiday wish lists",
                    "Tournament prizes/rewards",
                    "Limited edition/exclusivity"
                ],
                emotional_drivers=[
                    "Peer belonging (strongest driver)",
                    "Achievement & mastery",
                    "Status among friends",
                    "Curiosity & novelty",
                    "Pride in collection"
                ],
                brand_values=[
                    "Cool/fun factor (most important)",
                    "Quality that impresses friends",
                    "Fairness (no pay-to-win feeling)",
                    "Interactive/engaging",
                    "Authenticity to characters/story"
                ],
                nostalgia_references=[
                    "Current Pokémon (Scarlet/Violet era)",
                    "Naruto/My Hero Academia",
                    "Minecraft",
                    "Roblox",
                    "Among Us"
                ],
                skepticism_level="LOW",
                brand_loyalty="MEDIUM"
            ),

            AudienceSegment.GEN_ALPHA_OLD: AudiencePersona(
                segment=AudienceSegment.GEN_ALPHA_OLD,
                core_motivations=[
                    "Competitive achievement",
                    "Social status & identity expression",
                    "Skill development with visible progress",
                    "Independence from parents",
                    "Building unique personal brand"
                ],
                pain_points=[
                    "Golf seen as 'old people sport' by peers",
                    "Need independence but rely on parents financially",
                    "Want authentic experiences, not kids stuff",
                    "Peer judgment is harsh",
                    "Limited disposable income (allowance/part-time jobs)"
                ],
                aspirations=[
                    "Stand out with unique interests",
                    "Earn money/financial independence",
                    "Build valuable collections (investment mindset emerging)",
                    "Be taken seriously by adults",
                    "Excel at something that matters"
                ],
                media_consumption=[
                    "YouTube (deep dives, strategy)",
                    "TikTok (discovery & trends)",
                    "Instagram (identity expression)",
                    "Discord (communities)",
                    "Reddit (lurking, learning)"
                ],
                purchase_triggers=[
                    "Peer validation (what friends respect)",
                    "Influencer endorsement (authentic only)",
                    "Investment/resale value",
                    "Competitive advantage (helps me win)",
                    "Quality that lasts (anti-disposable)"
                ],
                emotional_drivers=[
                    "Identity formation (who am I?)",
                    "Competence & mastery",
                    "Autonomy & independence",
                    "Status & respect",
                    "Purpose & meaning"
                ],
                brand_values=[
                    "Authenticity (anti-fake)",
                    "Quality & durability",
                    "Respect for intelligence (don't talk down)",
                    "Innovation & uniqueness",
                    "Environmental/social consciousness"
                ],
                nostalgia_references=[
                    "Pokémon (current + older gens)",
                    "Anime (Demon Slayer, Attack on Titan, My Hero Academia)",
                    "Fortnite (earlier seasons)",
                    "Minecraft (classic)",
                    "Marvel/DC"
                ],
                skepticism_level="MEDIUM",
                brand_loyalty="LOW"
            ),

            AudienceSegment.PARENT_BUYERS: AudiencePersona(
                segment=AudienceSegment.PARENT_BUYERS,
                core_motivations=[
                    "Child's development & happiness",
                    "Quality family time & bonding",
                    "Educational value (justify purchase)",
                    "Building life skills in children",
                    "Being a 'good parent' (social validation)"
                ],
                pain_points=[
                    "Guilt over screen time vs outdoor activities",
                    "Budget constraints (kids are expensive)",
                    "Skeptical of fads/low-quality toys",
                    "Want products that last/have value",
                    "Tired of kids losing interest quickly"
                ],
                aspirations=[
                    "Raise well-rounded, skilled children",
                    "Share hobbies with kids (bonding)",
                    "Teach valuable life lessons through activities",
                    "Keep kids active & outdoors",
                    "Build family traditions & memories"
                ],
                media_consumption=[
                    "Facebook (parenting groups)",
                    "Instagram (family lifestyle)",
                    "YouTube (parent influencers, product reviews)",
                    "Email newsletters (parenting tips)",
                    "Mom/Dad blogs & forums"
                ],
                purchase_triggers=[
                    "Educational value (strongest for justification)",
                    "Peer parent recommendations",
                    "Child's persistent requests",
                    "Multi-use/longevity (worth the investment)",
                    "Positive reviews from other parents"
                ],
                emotional_drivers=[
                    "Love & care for child",
                    "Pride in child's achievements",
                    "Guilt relief (I'm doing the right thing)",
                    "Nostalgia (sharing my childhood passions)",
                    "Social validation (other parents approve)"
                ],
                brand_values=[
                    "Safety & quality (non-negotiable)",
                    "Educational value",
                    "Durability & longevity",
                    "Positive values (teamwork, sportsmanship)",
                    "Transparency & honesty"
                ],
                nostalgia_references=[
                    "Original Pokémon (their childhood)",
                    "Classic sports trading cards",
                    "Family golf outings (positive memories)",
                    "Collectibles they had as kids",
                    "90s/2000s culture"
                ],
                skepticism_level="HIGH",
                brand_loyalty="HIGH"
            )
        }

    def _initialize_frameworks(self) -> Dict[PsychologyFramework, Dict]:
        """Initialize psychology framework database"""
        return {
            PsychologyFramework.CIALDINI: {
                "name": "Cialdini's 6 Principles of Persuasion",
                "principles": {
                    "Reciprocity": "Give value first (free content, tips, community access)",
                    "Commitment": "Small commitments lead to big ones (follow → engage → purchase)",
                    "Social Proof": "Show others collecting, using, enjoying",
                    "Authority": "Expert golfers, pro endorsements, skill validation",
                    "Liking": "Relatable brand personality, shared values",
                    "Scarcity": "Limited editions, exclusive drops, Genesis sets"
                },
                "application": "Use scarcity for launches, social proof for community building"
            },

            PsychologyFramework.SELF_DETERMINATION: {
                "name": "Self-Determination Theory (Motivation)",
                "principles": {
                    "Autonomy": "Choice in which Crestline to collect, how to use cards",
                    "Competence": "Cards improve golf skill, progression system",
                    "Relatedness": "Community of collectors, shared identity"
                },
                "application": "Create progression system that increases competence while maintaining autonomy"
            },

            PsychologyFramework.GAMIFICATION: {
                "name": "Gamification (Octalysis Framework)",
                "core_drives": {
                    "Epic Meaning": "Be part of Line Energy mythology, chosen guardian",
                    "Accomplishment": "Complete sets, unlock achievements, level up",
                    "Empowerment": "Create content, share trick shots, personalize",
                    "Ownership": "Build YOUR collection, YOUR Crestline identity",
                    "Social Influence": "Compare collections, trade, compete",
                    "Scarcity": "Limited edition Crestlines, rare characters",
                    "Unpredictability": "Mystery packs, random drops, surprise unlocks",
                    "Avoidance": "FOMO on limited releases"
                },
                "application": "Layer multiple drives - don't rely on just scarcity or points"
            },

            PsychologyFramework.IDENTITY: {
                "name": "Identity Theory (Collectibles)",
                "principles": {
                    "Self-Expression": "Which Crestline are you?",
                    "Tribal Belonging": "Crestline community, not just customers",
                    "Status Signaling": "Rare cards signal dedication/taste",
                    "Narrative Identity": "Your Crestline tells your golf journey"
                },
                "application": "Make collecting part of personal identity, not just ownership"
            },

            PsychologyFramework.FOGG: {
                "name": "Fogg Behavior Model (B=MAT)",
                "formula": "Behavior = Motivation × Ability × Trigger",
                "components": {
                    "Motivation": "Create emotional desire (nostalgia, achievement, belonging)",
                    "Ability": "Make purchase easy (clear pricing, accessible)",
                    "Trigger": "Timely prompts (limited drops, influencer posts, FOMO)"
                },
                "application": "High motivation alone won't convert - need easy purchase + timely trigger"
            }
        }

    def analyze_name_phonetics(self, name: str) -> PhoneticAnalysis:
        """Analyze phonetic properties of a brand name"""
        name_lower = name.lower()

        # Extract phonetic elements
        initial = name[0].upper()
        syllables = self._count_syllables(name)
        hard_cons = [c for c in name.upper() if c in 'KGPTDBCQ']
        vowels = [c for c in name_lower if c in 'aeiou']

        # Calculate scores based on research
        # Hard consonants (K, G, P, T, D, B) improve recall
        memorability = min(10, 5 + len(hard_cons) * 1.5)

        # 2-3 syllables optimal
        if syllables in [2, 3]:
            pronunciation = 9.0
        elif syllables == 4:
            pronunciation = 7.0
        else:
            pronunciation = 5.0

        # Global friendliness (easy to pronounce across languages)
        # Penalize complex consonant clusters
        global_score = 8.0
        if 'th' in name_lower or 'ph' in name_lower:
            global_score -= 1.0
        if any(name_lower[i:i+3].replace('a','').replace('e','').replace('i','').replace('o','').replace('u','') for i in range(len(name_lower)-2)):
            global_score -= 1.5  # Consonant clusters

        rhythm = "Strong" if len(hard_cons) >= 2 else "Soft"

        return PhoneticAnalysis(
            initial_consonant=initial,
            syllable_count=syllables,
            hard_consonants=hard_cons,
            vowel_sounds=vowels,
            rhythm_pattern=rhythm,
            memorability_score=memorability,
            pronunciation_ease=pronunciation,
            global_friendliness=global_score
        )

    def _count_syllables(self, word: str) -> int:
        """Estimate syllable count"""
        word = word.lower()
        count = 0
        vowels = 'aeiou'
        previous_was_vowel = False

        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                count += 1
            previous_was_vowel = is_vowel

        # Adjust for silent e
        if word.endswith('e'):
            count -= 1

        # Ensure at least 1 syllable
        if count == 0:
            count = 1

        return count

    def score_brand_name(self, name: str, category: str = "golf collectibles") -> BrandNameScore:
        """Comprehensive brand name scoring"""

        # Phonetic analysis
        phonetic = self.analyze_name_phonetics(name)
        phonetic_score = phonetic.overall_score()

        # Emotional valence (-10 to +10)
        # Based on word associations
        positive_indicators = ['zen', 'flow', 'crest', 'line', 'peak', 'elite', 'master']
        negative_indicators = ['fail', 'weak', 'lose', 'bad']

        valence = 5.0  # Neutral baseline
        name_lower = name.lower()
        for word in positive_indicators:
            if word in name_lower:
                valence += 2.0
        for word in negative_indicators:
            if word in name_lower:
                valence -= 3.0

        # Uniqueness (0-10)
        # Penalize common words, reward invented terms
        common_words = ['golf', 'card', 'game', 'play', 'sport']
        uniqueness = 7.0
        for word in common_words:
            if word in name_lower:
                uniqueness -= 2.0

        # SEO potential
        # Short names with keywords rank better
        seo = 7.0
        if len(name) <= 8:
            seo += 1.5
        if 'golf' in name_lower or 'line' in name_lower:
            seo += 1.0
        seo = min(10, seo)

        # Social shareability (hashtag-friendly)
        social = 8.0
        if len(name) <= 10:
            social += 1.0
        if ' ' not in name:  # Single word better for hashtags
            social += 1.0
        social = min(10, social)

        # Generational appeal (based on research data)
        gen_appeal = {
            "Gen Z (18-28)": self._calculate_gen_z_appeal(name),
            "Millennials (29-40)": self._calculate_millennial_appeal(name),
            "Gen X (41+)": self._calculate_gen_x_appeal(name)
        }

        # Category fit for golf collectibles
        category_fit = 7.0
        if 'line' in name_lower or 'crest' in name_lower:
            category_fit += 2.0
        category_fit = min(10, category_fit)

        # Expandability (can it grow beyond golf?)
        expandability = 5.0
        if 'golf' not in name_lower:
            expandability += 3.0
        if name_lower in ['crestline', 'zenith', 'nexus', 'flux']:
            expandability += 2.0
        expandability = min(10, expandability)

        # Trademark risk assessment (simplified)
        trademark_risk = self._assess_trademark_risk(name)

        # Overall score (weighted average)
        weights = {
            'phonetic': 0.15,
            'emotional': 0.10,
            'uniqueness': 0.12,
            'seo': 0.10,
            'social': 0.15,
            'generational': 0.20,
            'category': 0.10,
            'expandability': 0.08
        }

        gen_avg = sum(gen_appeal.values()) / len(gen_appeal)

        overall = (
            phonetic_score * weights['phonetic'] +
            (valence + 10) / 2 * weights['emotional'] +  # Normalize to 0-10
            uniqueness * weights['uniqueness'] +
            seo * weights['seo'] +
            social * weights['social'] +
            gen_avg * weights['generational'] +
            category_fit * weights['category'] +
            expandability * weights['expandability']
        )

        return BrandNameScore(
            name=name,
            phonetic_score=round(phonetic_score, 2),
            emotional_valence=round(valence, 2),
            uniqueness_score=round(uniqueness, 2),
            trademark_risk=trademark_risk,
            seo_potential=round(seo, 2),
            social_shareability=round(social, 2),
            generational_appeal={k: round(v, 2) for k, v in gen_appeal.items()},
            category_fit=round(category_fit, 2),
            expandability=round(expandability, 2),
            overall_score=round(overall, 2)
        )

    def _calculate_gen_z_appeal(self, name: str) -> float:
        """Calculate Gen Z appeal (18-28)"""
        score = 5.0
        name_lower = name.lower()

        # Prefer short, punchy names
        if len(name) <= 7:
            score += 2.0

        # Prefer mystical/anime-style over traditional
        mystical_words = ['zen', 'flux', 'aura', 'nexus', 'crest', 'line']
        for word in mystical_words:
            if word in name_lower:
                score += 1.5

        # Penalize obviously golf-related
        if 'golf' in name_lower or 'green' in name_lower:
            score -= 2.0

        # Reward TikTok-friendly (catchy, hashtaggable)
        if len(name) <= 9 and ' ' not in name:
            score += 1.0

        return min(10, max(0, score))

    def _calculate_millennial_appeal(self, name: str) -> float:
        """Calculate Millennial appeal (29-40)"""
        score = 6.0
        name_lower = name.lower()

        # Appreciate nostalgia + quality signals
        quality_words = ['crest', 'elite', 'master', 'zenith', 'line']
        for word in quality_words:
            if word in name_lower:
                score += 1.0

        # Moderate length okay
        if 6 <= len(name) <= 12:
            score += 1.0

        # Golf connection okay but not required
        if 'golf' in name_lower:
            score += 0.5

        return min(10, max(0, score))

    def _calculate_gen_x_appeal(self, name: str) -> float:
        """Calculate Gen X appeal (41+)"""
        score = 5.0
        name_lower = name.lower()

        # Prefer clear, descriptive names
        if 'golf' in name_lower or 'green' in name_lower:
            score += 2.0

        # Appreciate heritage/traditional signals
        traditional_words = ['crest', 'club', 'master', 'classic']
        for word in traditional_words:
            if word in name_lower:
                score += 1.0

        # Moderate length preferred
        if 8 <= len(name) <= 14:
            score += 1.0

        return min(10, max(0, score))

    def _assess_trademark_risk(self, name: str) -> str:
        """Assess trademark risk level"""
        name_lower = name.lower()

        # Very common words = higher risk
        high_risk_words = ['golf', 'master', 'pro', 'club', 'card']
        medium_risk_words = ['line', 'crest', 'elite', 'sport']

        if any(word in name_lower for word in high_risk_words):
            return "MEDIUM-HIGH"
        elif any(word in name_lower for word in medium_risk_words):
            return "MEDIUM"
        else:
            return "LOW-MEDIUM"

    def generate_marketing_script(
        self,
        platform: Platform,
        segment: AudienceSegment,
        product_name: str = "Crestline",
        hook_type: str = "mystery"
    ) -> Dict[str, str]:
        """Generate platform-specific marketing scripts based on audience psychology"""

        persona = self.audience_personas[segment]

        scripts = {
            Platform.TIKTOK: self._generate_tiktok_script(persona, product_name, hook_type),
            Platform.INSTAGRAM_REELS: self._generate_instagram_reels_script(persona, product_name, hook_type),
            Platform.YOUTUBE_SHORTS: self._generate_youtube_shorts_script(persona, product_name, hook_type),
            Platform.INSTAGRAM_POST: self._generate_instagram_post(persona, product_name, hook_type),
            Platform.TWITTER: self._generate_twitter_script(persona, product_name, hook_type),
            Platform.EMAIL: self._generate_email_script(persona, product_name, hook_type)
        }

        return scripts[platform]

    def _generate_tiktok_script(self, persona: AudiencePersona, product: str, hook: str) -> Dict[str, str]:
        """Generate TikTok script (15-60s video)"""

        # Gen Z wants authenticity, fast pacing, no corporate speak
        if persona.segment in [AudienceSegment.GEN_Z_YOUNG, AudienceSegment.GEN_Z_OLD]:
            hook_line = "POV: You just unlocked a Crestline card and—wait for it—"
            body = """*Shows the card with die-cut design*
Your putting game just leveled up. But here's the thing...

*Scans QR code*

This isn't just a golf tool. Each Crestline card unlocks a character in the Line Energy universe.

*Shows AR character appearing*

Kai. Blaze. Luna. Torque.
Each one masters a different part of the game.

And yeah, you can actually use this on the green.

*Demonstrates alignment*

So... which Crestline are you? 👀

#Crestline #GolfTok #LineEnergy #CollectibleCards"""

        else:  # Millennials
            hook_line = "Remember collecting Pokémon cards? This is that... but for golf."
            body = """*Opens Crestline pack*

Premium PVC cards. Die-cut design.
Actually helps you read putts.

*Scans QR code*

But then you meet your character.

Kai—the master of precision.
Blaze—pure power.

Each card is a portal to the Line Energy universe.

Physical collectible. Digital experience. Real golf improvement.

Genesis set dropping soon 👇

#Crestline #GolfCollectibles #Nostalgia"""

        return {
            "platform": "TikTok",
            "format": "15-30 second video",
            "hook": hook_line,
            "body": body,
            "cta": "Link in bio for early access",
            "psychology_principles": [
                "Curiosity gap (what happens when you scan?)",
                "Social proof (which one are you?)",
                "Scarcity (Genesis set dropping soon)",
                f"Nostalgia ({persona.nostalgia_references[0]})"
            ],
            "visual_direction": "Fast cuts, close-ups of card details, AR effect reveal, putting demo"
        }

    def _generate_instagram_reels_script(self, persona: AudiencePersona, product: str, hook: str) -> Dict[str, str]:
        """Generate Instagram Reels script"""

        hook_line = "What if your golf alignment tool was also a collectible character card? 🎴⛳"

        body = """*Aesthetic flat lay of 4 Crestline cards*

Meet the Crestline Genesis Set.

*Pick up Kai card*
Kai - The Puttmaster. Precision. Focus. Control.

*Show die-cut alignment feature*
Use it on the green to read your line.

*Scan QR code - screen shows AR character*
Scan it to unlock your guardian in the Line Energy universe.

*Show all 4 characters together*
Kai. Blaze. Luna. Torque.

Which one matches your golf style?

Collect. Train. Evolve. 🌟

#Crestline #GolfCollectibles #LineEnergy #CollectibleCards #GolfLife"""

        return {
            "platform": "Instagram Reels",
            "format": "30-60 second video",
            "hook": hook_line,
            "body": body,
            "cta": "Drop a ⛳ if you want early access",
            "psychology_principles": [
                "Identity (which one are you?)",
                "Visual appeal (aesthetic)",
                "Dual utility (function + collectible)",
                "Completion desire (collect all 4)"
            ],
            "visual_direction": "High-quality cinematography, smooth transitions, aesthetic color grading"
        }

    def _generate_youtube_shorts_script(self, persona: AudiencePersona, product: str, hook: str) -> Dict[str, str]:
        """Generate YouTube Shorts script"""

        hook_line = "This golf card just changed my putting game forever..."

        body = """*On golf course with Crestline card*

So I got this thing called a Crestline card.

*Show card close-up*

It's got this die-cut design that helps you align your putts.

*Demonstrate on green*

Already cool, right?

*Pull out phone*

But then you scan the QR code...

*Show AR character Kai appearing*

And you unlock Kai—the Puttmaster—in the Line Energy universe.

There are 4 founding characters:
- Kai (precision)
- Blaze (power)
- Luna (strategy)
- Torque (adaptability)

*Show all 4 cards*

It's like Pokémon met golf and I'm here for it.

Genesis set launching soon—link below 👇"""

        return {
            "platform": "YouTube Shorts",
            "format": "30-60 second video",
            "hook": hook_line,
            "body": body,
            "cta": "Link in description for early access",
            "psychology_principles": [
                "Curiosity (what happens when you scan?)",
                "Demonstration (proof it works)",
                "Familiar analogy (Pokémon comparison)",
                "Scarcity (launching soon)"
            ],
            "visual_direction": "POV style, casual vibe, on-course demonstration"
        }

    def _generate_instagram_post(self, persona: AudiencePersona, product: str, hook: str) -> Dict[str, str]:
        """Generate Instagram carousel post"""

        caption = """The Line Energy has awakened. ⚡🎴

Introducing Crestline—where golf meets power.

Swipe to meet the 4 Founding Guardians:

1️⃣ KAI - The Puttmaster
Calm. Precise. Master of the green.
Special ability: Perfect Line Reading

2️⃣ BLAZE - The Driver X
Fiery. Explosive. Master of distance.
Special ability: Maximum Power Drive

3️⃣ LUNA - The Wind Whisperer
Strategic. Elegant. Master of flight.
Special ability: Wind Control

4️⃣ TORQUE - The Gearshaper
Adaptive. Inventive. Master of mechanics.
Special ability: Spin Manipulation

Each Crestline card is:
✅ Premium PVC collectible with original artwork
✅ Functional putting alignment tool
✅ Gateway to digital content (scan QR code)
✅ Part of the Line Energy mythology

Genesis Set drops [DATE]
Limited first edition.

Which Crestline Guardian matches your golf style? Comment below 👇

#Crestline #LineEnergy #GolfCollectibles #CollectibleCards #GolfCommunity #AnimeGolf #Golformers"""

        return {
            "platform": "Instagram Post",
            "format": "Carousel (5 images)",
            "images": [
                "1. All 4 cards arranged artistically",
                "2. Kai card close-up with character art",
                "3. Blaze card close-up",
                "4. Luna card close-up",
                "5. Torque card close-up",
                "6. Card being used on golf green (bonus)"
            ],
            "caption": caption,
            "cta": "Link in bio for early access",
            "psychology_principles": [
                "Identity (which guardian are you?)",
                "Completionist (collect all 4)",
                "Social proof (community)",
                "Scarcity (limited first edition)",
                "Epic meaning (Line Energy mythology)"
            ]
        }

    def _generate_twitter_script(self, persona: AudiencePersona, product: str, hook: str) -> Dict[str, str]:
        """Generate Twitter/X thread"""

        thread = """🧵 We're launching something that merges golf, anime culture, and collectibles in a way that's never been done.

Meet Crestline. 🎴⛳

(1/8)

---

The concept: What if your golf alignment tool was also a gateway to a universe of powered-up characters?

Each Crestline card serves TWO purposes:
• Physical: Precision putting aid
• Digital: Unlock your guardian in the Line Energy universe

(2/8)

---

The Founding Four:

⚡ KAI - The Puttmaster (Precision)
🔥 BLAZE - The Driver X (Power)
🌙 LUNA - The Wind Whisperer (Strategy)
⚙️ TORQUE - The Gearshaper (Adaptability)

Each masters one aspect of golf... with supernatural skill.

(3/8)

---

The mythology:

"Line Energy" is a mysterious force flowing through every golf course on Earth.

The Crestline Guardians channel this energy to transcend normal golf abilities.

Your card connects you to their power. 🌟

(4/8)

---

The experience:

1. Get your Crestline card
2. Use it on the green (die-cut design aids alignment)
3. Scan QR code → meet your guardian
4. Access training tips, AR effects, challenges
5. Level up your "Line Energy"

Physical + Digital = Complete experience

(5/8)

---

Why we built this:

Golf has untapped creative potential.

The next generation wants:
• Characters they connect with
• Communities they belong to
• Tools that are both functional AND meaningful

Crestline is all three. 🎯

(6/8)

---

The vision:

Genesis Set (4 founding guardians) → drops [DATE]

Future:
• Expanded character roster
• Crestline League tournaments
• Digital companion app
• Animated content series

This is just the beginning. 🚀

(7/8)

---

Question for golf + collectible fans:

Which guardian would you want in your bag?

⚡ Kai (Precision)
🔥 Blaze (Power)
🌙 Luna (Strategy)
⚙️ Torque (Adaptability)

Drop your choice below 👇

Early access: [LINK]

(8/8)"""

        return {
            "platform": "Twitter/X",
            "format": "Thread (8 tweets)",
            "thread": thread,
            "cta": "Early access link in final tweet",
            "psychology_principles": [
                "Curiosity gap (something never been done)",
                "Story-driven (mythology)",
                "Social proof (which guardian?)",
                "Vision casting (future roadmap)",
                "Engagement prompt (poll-style question)"
            ]
        }

    def _generate_email_script(self, persona: AudiencePersona, product: str, hook: str) -> Dict[str, str]:
        """Generate email marketing campaign"""

        subject_lines = [
            "Your Crestline Guardian awaits ⚡",
            "Golf + Anime + Collectibles = ?",
            "[FIRST LOOK] The Crestline Genesis Set",
            "Which Crestline Guardian are you?",
            "Exclusive: Line Energy has awakened 🎴"
        ]

        body = """Subject: [FIRST LOOK] The Crestline Genesis Set

---

Hey [First Name],

You're getting this because you signed up to hear about something... different.

**The short version:**
We're launching collectible cards that actually improve your golf game and unlock a digital universe of powered-up characters.

**The longer version:**

Imagine if Pokémon and golf had a baby, raised by anime culture and premium design.

That's Crestline.

---

**WHAT IT IS:**

Each Crestline card is:
• A premium PVC collectible with original character artwork
• A functional putting alignment tool (die-cut precision design)
• A portal to the Line Energy digital universe (scan QR code)

---

**THE FOUNDING FOUR:**

⚡ **KAI** - The Puttmaster
Master of precision. Calm under pressure. Your green-reading mentor.

🔥 **BLAZE** - The Driver X
Master of power. Explosive energy. Your distance coach.

🌙 **LUNA** - The Wind Whisperer
Master of strategy. Reads the course like poetry. Your tactical advisor.

⚙️ **TORQUE** - The Gearshaper
Master of adaptability. Inventor spirit. Your all-conditions guide.

---

**THE MYTHOLOGY:**

"Line Energy" flows through every golf course on Earth—a mysterious force that, when channeled, grants supernatural golf abilities.

The Crestline Guardians are legendary golfers who've mastered this energy.

When you hold a Crestline card, you connect to their power.

---

**THE EXPERIENCE:**

1. **Collect** - Premium card in hand
2. **Use** - Align your putts with precision die-cut design
3. **Scan** - QR code unlocks your guardian
4. **Train** - Access tips, AR effects, challenges
5. **Evolve** - Level up your Line Energy, unlock rewards

---

**GENESIS SET DETAILS:**

🎴 4 founding guardians
📅 Launching: [DATE]
🎯 Limited first edition (numbered)
💳 Price: $[XX] per card / $[XX] complete set
🎁 Early Access Bonus: [Exclusive perk for email list]

---

**YOUR NEXT STEP:**

We're giving email subscribers **48-hour early access** before the public launch.

**[RESERVE YOUR CRESTLINE SET]** ← Click here

Once they're gone, they're gone. This is the Genesis Set—we won't reprint these exact editions.

---

**One question before you go:**

Which guardian matches your golf style?

Hit reply and tell me. I read every response.

⚡ Kai (Precision)
🔥 Blaze (Power)
🌙 Luna (Strategy)
⚙️ Torque (Adaptability)

Let's build this together.

—[Your Name]
Founder, Crestline

P.S. - Still not sure? Check out this [2-min video] showing the cards in action on a real golf course. The AR reveal is 🔥

---

**SOCIAL PROOF SECTION (optional):**

"This is exactly what golf needs right now—creativity and culture."
— @GolfInfluencer, 250K followers

"I showed my kids and they actually want to learn golf now. That's a first."
— Early tester

"The card quality is insane. This isn't cheap merch—it's premium collectible."
— Beta collector

---"""

        return {
            "platform": "Email",
            "format": "Launch announcement email",
            "subject_lines": subject_lines,
            "body": body,
            "cta": "Reserve Your Crestline Set (Early Access)",
            "psychology_principles": [
                "Exclusivity (email list early access)",
                "Scarcity (limited first edition)",
                "Story-driven (mythology)",
                "Social proof (testimonials)",
                "Reciprocity (exclusive bonus)",
                "Personal connection (reply prompt)"
            ],
            "follow_up_sequence": [
                "Email 2 (24h later): Customer testimonial + FAQ",
                "Email 3 (48h later): Last chance early access",
                "Email 4 (Launch day): Public launch announcement",
                "Email 5 (3 days post): First batch shipping update"
            ]
        }

    def compare_names(self, names: List[str]) -> Dict[str, BrandNameScore]:
        """Compare multiple brand names side by side"""
        results = {}
        for name in names:
            results[name] = self.score_brand_name(name)
        return results

    def generate_persona_report(self, segment: AudienceSegment) -> str:
        """Generate detailed persona report"""
        persona = self.audience_personas[segment]

        report = f"""
========================================
AUDIENCE PERSONA REPORT
========================================
Segment: {persona.segment.value}

CORE MOTIVATIONS:
{self._format_list(persona.core_motivations)}

PAIN POINTS:
{self._format_list(persona.pain_points)}

ASPIRATIONS:
{self._format_list(persona.aspirations)}

MEDIA CONSUMPTION:
{self._format_list(persona.media_consumption)}

PURCHASE TRIGGERS:
{self._format_list(persona.purchase_triggers)}

EMOTIONAL DRIVERS:
{self._format_list(persona.emotional_drivers)}

BRAND VALUES:
{self._format_list(persona.brand_values)}

NOSTALGIA REFERENCES:
{self._format_list(persona.nostalgia_references)}

SKEPTICISM LEVEL: {persona.skepticism_level}
BRAND LOYALTY: {persona.brand_loyalty}

========================================
STRATEGIC RECOMMENDATIONS:
========================================
Based on this persona:

1. MESSAGING TONE:
   {"Authentic, casual, no corporate speak" if persona.skepticism_level == "HIGH" else "Professional but approachable"}

2. CONTENT STRATEGY:
   Primary channels: {', '.join(persona.media_consumption[:3])}

3. CONVERSION TACTICS:
   Focus on: {', '.join(persona.purchase_triggers[:3])}

4. BRAND POSITIONING:
   Emphasize: {', '.join(persona.brand_values[:3])}
========================================
"""
        return report

    def _format_list(self, items: List[str]) -> str:
        """Format list items with bullets"""
        return '\n'.join([f"  • {item}" for item in items])

    def export_analysis(self, filename: str = "crestline_marketing_analysis.json"):
        """Export all analysis data to JSON"""
        data = {
            "personas": {seg.value: asdict(persona) for seg, persona in self.audience_personas.items()},
            "frameworks": {fw.value: details for fw, details in self.psychology_frameworks.items()}
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2, default=str)

        return f"Analysis exported to {filename}"


def main():
    """Main CLI interface for the marketing tool"""

    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        CRESTLINE MARKETING PSYCHOLOGY TOOL v1.0              ║
║                                                               ║
║     Brand Name Analysis • Audience Psychology                ║
║     Script Generation • Strategic Frameworks                  ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)

    tool = MarketingPsychologyTool()

    print("\n🎯 BRAND NAME ANALYSIS\n" + "="*60)

    # Compare key name options
    names_to_test = [
        "Crestline",
        "Greencrest",
        "Lineum",
        "Zenith",
        "Lineblade",
        "Golformers"
    ]

    print("\nComparing brand name candidates...\n")

    scores = tool.compare_names(names_to_test)

    # Sort by overall score
    sorted_names = sorted(scores.items(), key=lambda x: x[1].overall_score, reverse=True)

    print(f"{'RANK':<6} {'NAME':<15} {'OVERALL':<10} {'PHONETIC':<10} {'GEN Z':<10} {'MILLENNIAL':<12} {'SOCIAL':<10}")
    print("-" * 85)

    for i, (name, score) in enumerate(sorted_names, 1):
        gen_z_score = score.generational_appeal.get("Gen Z (18-28)", 0)
        mill_score = score.generational_appeal.get("Millennials (29-40)", 0)
        print(f"{i:<6} {name:<15} {score.overall_score:<10.2f} {score.phonetic_score:<10.2f} {gen_z_score:<10.2f} {mill_score:<12.2f} {score.social_shareability:<10.2f}")

    # Detailed report for top pick
    top_name = sorted_names[0][0]
    top_score = sorted_names[0][1]

    print(f"\n\n🏆 TOP RECOMMENDATION: {top_name.upper()}")
    print("="*60)
    print(f"Overall Score: {top_score.overall_score}/10")
    print(f"\nSTRENGTHS:")
    print(f"  • Phonetic Power: {top_score.phonetic_score}/10")
    print(f"  • Social Shareability: {top_score.social_shareability}/10")
    print(f"  • SEO Potential: {top_score.seo_potential}/10")
    print(f"  • Expandability: {top_score.expandability}/10")
    print(f"\nGENERATIONAL APPEAL:")
    for gen, score_val in top_score.generational_appeal.items():
        print(f"  • {gen}: {score_val}/10")
    print(f"\nTrademark Risk: {top_score.trademark_risk}")

    # Audience personas
    print("\n\n🧠 TARGET AUDIENCE ANALYSIS\n" + "="*60)

    primary_segment = AudienceSegment.GEN_Z_OLD
    print(f"\nPRIMARY TARGET: {primary_segment.value}")
    print(tool.generate_persona_report(primary_segment))

    # Marketing scripts
    print("\n\n📱 MARKETING SCRIPT SAMPLES\n" + "="*60)

    print("\n--- TIKTOK SCRIPT (Gen Z) ---")
    tiktok_script = tool.generate_marketing_script(
        Platform.TIKTOK,
        AudienceSegment.GEN_Z_OLD,
        product_name="Crestline",
        hook_type="mystery"
    )
    print(f"\nHOOK: {tiktok_script['hook']}")
    print(f"\nBODY:\n{tiktok_script['body']}")
    print(f"\nCTA: {tiktok_script['cta']}")
    print(f"\nPSYCHOLOGY PRINCIPLES:")
    for principle in tiktok_script['psychology_principles']:
        print(f"  ✓ {principle}")

    print("\n\n--- INSTAGRAM POST (Millennial) ---")
    ig_post = tool.generate_marketing_script(
        Platform.INSTAGRAM_POST,
        AudienceSegment.MILLENNIAL_YOUNG,
        product_name="Crestline"
    )
    print(f"\nCAPTION:\n{ig_post['caption'][:500]}...")
    print(f"\nIMAGE SEQUENCE:")
    for img in ig_post['images']:
        print(f"  • {img}")

    # Export data
    print("\n\n💾 EXPORTING DATA...\n" + "="*60)
    export_file = tool.export_analysis("crestline_marketing_analysis.json")
    print(f"✓ {export_file}")

    print("\n\n✅ ANALYSIS COMPLETE!\n")
    print("Next steps:")
    print("  1. Review the brand name scores above")
    print("  2. Test top 3 names with real audience samples")
    print("  3. Use the generated scripts as templates for content creation")
    print("  4. Review the JSON export for detailed persona data")
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
