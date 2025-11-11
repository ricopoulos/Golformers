#!/usr/bin/env python3
"""
Target Audience Scenario Modeler
=================================
Interactive tool to test how different target audience choices affect:
- Brand name scores
- Messaging strategy
- Pricing recommendations
- Channel strategy

This lets you validate the 24-28 target or explore alternatives.
"""

from marketing_psychology_tool import (
    MarketingPsychologyTool,
    AudienceSegment,
    Platform
)
from dataclasses import dataclass
from typing import List, Dict
import json


@dataclass
class AudienceScenario:
    """A target audience scenario to model"""
    name: str
    primary_segment: AudienceSegment
    secondary_segment: AudienceSegment
    description: str
    market_size: int  # in thousands
    growth_rate: float  # annual %
    avg_purchase_power: int  # annual disposable income


class AudienceScenarioModeler:
    """Model different target audience scenarios"""

    def __init__(self):
        self.tool = MarketingPsychologyTool()
        self.scenarios = self._create_scenarios()

    def _create_scenarios(self) -> Dict[str, AudienceScenario]:
        """Define different audience scenarios to test"""
        return {
            "gen_z_focus": AudienceScenario(
                name="Gen Z Focus (24-28 Primary)",
                primary_segment=AudienceSegment.GEN_Z_OLD,
                secondary_segment=AudienceSegment.GEN_Z_YOUNG,
                description="Target Gen Z as growth engine, with younger Gen Z as future buyers",
                market_size=4000,  # 4M golfers
                growth_rate=0.55,  # 55% 5-year growth
                avg_purchase_power=30000
            ),

            "millennial_focus": AudienceScenario(
                name="Millennial Focus (29-34 Primary)",
                primary_segment=AudienceSegment.MILLENNIAL_YOUNG,
                secondary_segment=AudienceSegment.GEN_Z_OLD,
                description="Target Millennials with higher purchasing power, Gen Z as trendsetters",
                market_size=3000,  # 3M golfers
                growth_rate=0.35,  # 35% 5-year growth
                avg_purchase_power=45000
            ),

            "youth_focus": AudienceScenario(
                name="Youth Focus (18-23 Primary)",
                primary_segment=AudienceSegment.GEN_Z_YOUNG,
                secondary_segment=AudienceSegment.GEN_Z_OLD,
                description="Target youngest Gen Z for viral growth, accept lower initial revenue",
                market_size=2000,  # 2M golfers
                growth_rate=0.45,  # 45% 5-year growth
                avg_purchase_power=10000
            ),

            "premium_focus": AudienceScenario(
                name="Premium Focus (35-40 Primary)",
                primary_segment=AudienceSegment.MILLENNIAL_CORE,
                secondary_segment=AudienceSegment.MILLENNIAL_YOUNG,
                description="Target established Millennials with highest purchasing power",
                market_size=3500,  # 3.5M golfers
                growth_rate=0.15,  # 15% 5-year growth
                avg_purchase_power=60000
            ),

            "bridge_strategy": AudienceScenario(
                name="Bridge Strategy (24-34 Broad)",
                primary_segment=AudienceSegment.GEN_Z_OLD,
                secondary_segment=AudienceSegment.MILLENNIAL_YOUNG,
                description="Target both Gen Z and young Millennials as single cohort",
                market_size=7000,  # 7M combined
                growth_rate=0.45,  # Weighted average
                avg_purchase_power=37500  # Weighted average
            ),

            "family_strategy": AudienceScenario(
                name="Family Strategy (Juniors 10-17, Parents Buy)",
                primary_segment=AudienceSegment.PARENT_BUYERS,
                secondary_segment=AudienceSegment.GEN_ALPHA_OLD,
                description="Target parents buying for junior golfers - dual appeal to kids & parents",
                market_size=3700,  # 3.7M junior golfers (parents make purchases)
                growth_rate=0.48,  # 48% 5-year growth (HIGHEST of all segments!)
                avg_purchase_power=50000  # Parent income, not kids
            ),

            "gen_alpha_focus": AudienceScenario(
                name="Gen Alpha Direct (14-17 Direct Purchase)",
                primary_segment=AudienceSegment.GEN_ALPHA_OLD,
                secondary_segment=AudienceSegment.GEN_Z_YOUNG,
                description="Target older Gen Alpha with allowance/part-time job money",
                market_size=2000,  # ~2M older junior golfers
                growth_rate=0.48,  # Same high growth
                avg_purchase_power=2000  # Allowance + part-time jobs only
            )
        }

    def analyze_scenario(self, scenario_key: str) -> Dict:
        """Analyze a specific audience scenario"""
        scenario = self.scenarios[scenario_key]

        # Get persona data for primary segment
        primary_persona = self.tool.audience_personas[scenario.primary_segment]
        secondary_persona = self.tool.audience_personas[scenario.secondary_segment]

        # Score brand names for this audience mix
        names_to_test = ["Crestline", "Greencrest", "Lineum", "Zenith", "Lineblade", "Golformers"]
        name_scores = {}

        for name in names_to_test:
            score = self.tool.score_brand_name(name)
            # Calculate weighted score (70% primary, 30% secondary)
            primary_key = list(score.generational_appeal.keys())[0]  # Get first key as proxy

            # Map segments to generational appeal keys
            if scenario.primary_segment in [AudienceSegment.GEN_Z_YOUNG, AudienceSegment.GEN_Z_OLD]:
                primary_appeal = score.generational_appeal.get("Gen Z (18-28)", 5.0)
            else:
                primary_appeal = score.generational_appeal.get("Millennials (29-40)", 5.0)

            if scenario.secondary_segment in [AudienceSegment.GEN_Z_YOUNG, AudienceSegment.GEN_Z_OLD]:
                secondary_appeal = score.generational_appeal.get("Gen Z (18-28)", 5.0)
            else:
                secondary_appeal = score.generational_appeal.get("Millennials (29-40)", 5.0)

            weighted_appeal = (primary_appeal * 0.7) + (secondary_appeal * 0.3)

            name_scores[name] = {
                "overall": score.overall_score,
                "primary_appeal": primary_appeal,
                "secondary_appeal": secondary_appeal,
                "weighted_appeal": weighted_appeal,
                "social_shareability": score.social_shareability
            }

        # Calculate revenue potential (simplified model)
        # Revenue = Market Size × Conversion Rate × Avg Order Value
        conversion_rates = {
            AudienceSegment.GEN_ALPHA_YOUNG: 0.08,  # 8% (parents buy via kid requests)
            AudienceSegment.GEN_ALPHA_OLD: 0.05,    # 5% (limited own money)
            AudienceSegment.PARENT_BUYERS: 0.10,    # 10% (HIGH - parents justify as educational)
            AudienceSegment.GEN_Z_YOUNG: 0.02,      # 2% (lower purchasing power)
            AudienceSegment.GEN_Z_OLD: 0.04,        # 4% (best balance)
            AudienceSegment.MILLENNIAL_YOUNG: 0.035,  # 3.5% (higher skepticism)
            AudienceSegment.MILLENNIAL_CORE: 0.03,  # 3% (highest standards)
        }

        avg_order_values = {
            AudienceSegment.GEN_ALPHA_YOUNG: 50,   # Parents buy sets as gifts
            AudienceSegment.GEN_ALPHA_OLD: 25,     # Allowance purchases (singles)
            AudienceSegment.PARENT_BUYERS: 65,     # Family sets + educational justification
            AudienceSegment.GEN_Z_YOUNG: 45,       # Lower price point
            AudienceSegment.GEN_Z_OLD: 70,         # Mid-premium
            AudienceSegment.MILLENNIAL_YOUNG: 85,  # Premium willing
            AudienceSegment.MILLENNIAL_CORE: 120,  # Ultra-premium
        }

        primary_conversion = conversion_rates[scenario.primary_segment]
        primary_aov = avg_order_values[scenario.primary_segment]

        estimated_revenue = scenario.market_size * primary_conversion * primary_aov

        # Determine optimal pricing
        pricing_recs = self._get_pricing_recommendations(scenario)

        # Determine channel strategy
        channel_strategy = self._get_channel_strategy(primary_persona)

        # Determine messaging tone
        messaging_tone = self._get_messaging_tone(primary_persona)

        return {
            "scenario": scenario,
            "primary_persona": primary_persona,
            "secondary_persona": secondary_persona,
            "name_scores": name_scores,
            "best_name": max(name_scores.items(), key=lambda x: x[1]["weighted_appeal"])[0],
            "estimated_revenue_k": round(estimated_revenue, 0),
            "pricing_recommendations": pricing_recs,
            "channel_strategy": channel_strategy,
            "messaging_tone": messaging_tone,
            "growth_potential": scenario.growth_rate * 100,
            "competitive_advantage": self._assess_competitive_advantage(scenario)
        }

    def _get_pricing_recommendations(self, scenario: AudienceScenario) -> Dict:
        """Recommend pricing based on audience"""
        pricing = {
            AudienceSegment.GEN_ALPHA_YOUNG: {
                "single": "$9.99-12.99",
                "set_4": "$39.99-49.99",
                "special_edition": "$59.99-69.99",
                "rationale": "Parent-friendly pricing for birthday/holiday gifts, comparable to Pokémon packs"
            },
            AudienceSegment.GEN_ALPHA_OLD: {
                "single": "$12.99-15.99",
                "set_4": "$49.99-59.99",
                "special_edition": "$79.99-89.99",
                "rationale": "Allowance-accessible for singles, parent-bought sets for special occasions"
            },
            AudienceSegment.PARENT_BUYERS: {
                "single": "$12.99-14.99",
                "set_4": "$49.99-59.99",
                "special_edition": "$79.99-99.99",
                "rationale": "Educational premium - parents pay more for 'developmental' products"
            },
            AudienceSegment.GEN_Z_YOUNG: {
                "single": "$15-19",
                "set_4": "$45-55",
                "special_edition": "$69-79",
                "rationale": "Lower price point for student/early career buyers"
            },
            AudienceSegment.GEN_Z_OLD: {
                "single": "$19-24",
                "set_4": "$69-79",
                "special_edition": "$99-129",
                "rationale": "Mid-premium positioning, quality signal + accessible"
            },
            AudienceSegment.MILLENNIAL_YOUNG: {
                "single": "$24-29",
                "set_4": "$89-99",
                "special_edition": "$149-179",
                "rationale": "Premium positioning, emphasize quality + nostalgia"
            },
            AudienceSegment.MILLENNIAL_CORE: {
                "single": "$29-39",
                "set_4": "$119-149",
                "special_edition": "$199-299",
                "rationale": "Ultra-premium, collector's edition focus"
            }
        }
        return pricing[scenario.primary_segment]

    def _get_channel_strategy(self, persona) -> Dict:
        """Recommend marketing channels based on persona"""
        channels = persona.media_consumption
        return {
            "primary_channels": channels[:2],
            "secondary_channels": channels[2:4] if len(channels) > 2 else [],
            "channel_budget_allocation": {
                channels[0]: "40%",
                channels[1]: "30%",
                channels[2] if len(channels) > 2 else "other": "20%",
                "experimental": "10%"
            }
        }

    def _get_messaging_tone(self, persona) -> Dict:
        """Recommend messaging tone based on persona"""
        skepticism_mapping = {
            "HIGH": {
                "tone": "Authentic, casual, no corporate speak",
                "avoid": ["Hype", "Superlatives", "Hard sell", "Fake urgency"],
                "use": ["Real stories", "Behind-the-scenes", "Community voice", "Honest limitations"]
            },
            "MEDIUM": {
                "tone": "Professional but approachable, story-driven",
                "avoid": ["Overpromising", "Gimmicks", "Trendy slang"],
                "use": ["Quality focus", "Heritage", "Craftsmanship", "Value proposition"]
            },
            "LOW": {
                "tone": "Confident, traditional, authoritative",
                "avoid": ["Too casual", "Meme culture", "Experimental"],
                "use": ["Expertise", "Legacy", "Premium positioning", "Exclusivity"]
            }
        }
        return skepticism_mapping[persona.skepticism_level]

    def _assess_competitive_advantage(self, scenario: AudienceScenario) -> str:
        """Assess competitive positioning for this scenario"""
        advantages = {
            AudienceSegment.GEN_ALPHA_YOUNG: "Zero competition in junior golf collectibles, fastest growth segment (48%), Pokémon-model proven",
            AudienceSegment.GEN_ALPHA_OLD: "Fast growth + emerging purchasing power, bridge to Gen Z, tournament/camp B2B potential",
            AudienceSegment.PARENT_BUYERS: "HUGE whitespace - parents want golf products for kids, educational justification drives premium pricing, tournament prize market untapped",
            AudienceSegment.GEN_Z_YOUNG: "First-mover in Gen Z golf collectibles, high viral potential but lower immediate revenue",
            AudienceSegment.GEN_Z_OLD: "Optimal whitespace - golf interest + collectible nostalgia + spending power converge",
            AudienceSegment.MILLENNIAL_YOUNG: "Strong nostalgia play, premium willing, but more competitive landscape",
            AudienceSegment.MILLENNIAL_CORE: "Highest AOV potential but saturated market, harder to differentiate"
        }
        return advantages.get(scenario.primary_segment, "Unknown")

    def compare_all_scenarios(self) -> None:
        """Compare all scenarios side by side"""
        print("\n" + "="*100)
        print("TARGET AUDIENCE SCENARIO COMPARISON")
        print("="*100 + "\n")

        results = {}
        for key in self.scenarios.keys():
            results[key] = self.analyze_scenario(key)

        # Print comparison table
        print(f"{'SCENARIO':<25} {'BEST NAME':<15} {'EST. REVENUE':<15} {'GROWTH':<10} {'AVG APPEAL':<12}")
        print("-"*100)

        for key, result in results.items():
            scenario = result["scenario"]
            best_name = result["best_name"]
            revenue = result["estimated_revenue_k"]
            growth = result["growth_potential"]
            best_score = result["name_scores"][best_name]["weighted_appeal"]

            print(f"{scenario.name:<25} {best_name:<15} ${revenue:>10,.0f}K  {growth:>6.1f}%    {best_score:>5.2f}/10")

        # Detailed breakdown for each scenario
        print("\n" + "="*100)
        print("DETAILED SCENARIO ANALYSIS")
        print("="*100)

        for key, result in results.items():
            self._print_scenario_detail(result)

    def _print_scenario_detail(self, result: Dict) -> None:
        """Print detailed analysis for one scenario"""
        scenario = result["scenario"]

        print(f"\n{'='*80}")
        print(f"SCENARIO: {scenario.name}")
        print(f"{'='*80}")

        print(f"\n📊 MARKET DATA:")
        print(f"  • Market Size: {scenario.market_size:,} golfers")
        print(f"  • 5-Year Growth Rate: {scenario.growth_rate*100:.1f}%")
        print(f"  • Avg Purchase Power: ${scenario.avg_purchase_power:,}/year")
        print(f"  • Estimated Year 1 Revenue: ${result['estimated_revenue_k']:,.0f}K")

        print(f"\n🎯 TARGET SEGMENTS:")
        print(f"  • Primary: {scenario.primary_segment.value}")
        print(f"  • Secondary: {scenario.secondary_segment.value}")

        print(f"\n🏆 BRAND NAME RANKINGS:")
        sorted_names = sorted(
            result["name_scores"].items(),
            key=lambda x: x[1]["weighted_appeal"],
            reverse=True
        )
        for i, (name, scores) in enumerate(sorted_names[:5], 1):
            print(f"  {i}. {name:<15} Score: {scores['weighted_appeal']:.2f}/10 "
                  f"(Primary: {scores['primary_appeal']:.1f}, Secondary: {scores['secondary_appeal']:.1f})")

        print(f"\n💰 PRICING STRATEGY:")
        pricing = result["pricing_recommendations"]
        print(f"  • Single Card: {pricing['single']}")
        print(f"  • 4-Card Set: {pricing['set_4']}")
        print(f"  • Special Edition: {pricing['special_edition']}")
        print(f"  • Rationale: {pricing['rationale']}")

        print(f"\n📱 CHANNEL STRATEGY:")
        channels = result["channel_strategy"]
        print(f"  • Primary: {', '.join(channels['primary_channels'])}")
        print(f"  • Secondary: {', '.join(channels['secondary_channels'])}")
        print(f"  • Budget Split:")
        for channel, budget in channels['channel_budget_allocation'].items():
            print(f"    - {channel}: {budget}")

        print(f"\n💬 MESSAGING TONE:")
        tone = result["messaging_tone"]
        print(f"  • Tone: {tone['tone']}")
        print(f"  • Avoid: {', '.join(tone['avoid'][:3])}")
        print(f"  • Use: {', '.join(tone['use'][:3])}")

        print(f"\n🎯 COMPETITIVE ADVANTAGE:")
        print(f"  {result['competitive_advantage']}")

        print(f"\n📈 GROWTH POTENTIAL:")
        print(f"  {result['growth_potential']:.1f}% projected 5-year growth")

        print()

    def generate_scenario_report(self, scenario_key: str, filename: str = None) -> str:
        """Generate a detailed report for a specific scenario"""
        result = self.analyze_scenario(scenario_key)

        if filename is None:
            filename = f"scenario_{scenario_key}_report.json"

        # Convert to JSON-serializable format
        report = {
            "scenario_name": result["scenario"].name,
            "market_data": {
                "size": result["scenario"].market_size,
                "growth_rate": result["scenario"].growth_rate,
                "purchase_power": result["scenario"].avg_purchase_power,
                "estimated_revenue": result["estimated_revenue_k"]
            },
            "target_segments": {
                "primary": result["scenario"].primary_segment.value,
                "secondary": result["scenario"].secondary_segment.value
            },
            "brand_names": result["name_scores"],
            "best_name": result["best_name"],
            "pricing": result["pricing_recommendations"],
            "channels": result["channel_strategy"],
            "messaging": result["messaging_tone"],
            "competitive_advantage": result["competitive_advantage"]
        }

        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

        return f"Report saved to {filename}"

    def interactive_mode(self):
        """Run interactive scenario selection"""
        print("\n" + "="*80)
        print("INTERACTIVE TARGET AUDIENCE SCENARIO MODELER")
        print("="*80)

        print("\nAvailable scenarios:")
        for i, (key, scenario) in enumerate(self.scenarios.items(), 1):
            print(f"\n{i}. {scenario.name}")
            print(f"   {scenario.description}")

        print(f"\n{len(self.scenarios)+1}. Compare all scenarios")
        print(f"{len(self.scenarios)+2}. Exit")

        while True:
            try:
                choice = input(f"\nSelect scenario (1-{len(self.scenarios)+2}): ").strip()
                choice_num = int(choice)

                if choice_num == len(self.scenarios) + 2:
                    print("\nExiting...")
                    break
                elif choice_num == len(self.scenarios) + 1:
                    self.compare_all_scenarios()
                elif 1 <= choice_num <= len(self.scenarios):
                    scenario_key = list(self.scenarios.keys())[choice_num - 1]
                    result = self.analyze_scenario(scenario_key)
                    self._print_scenario_detail(result)

                    save = input("\nSave this report to JSON? (y/n): ").strip().lower()
                    if save == 'y':
                        filename = self.generate_scenario_report(scenario_key)
                        print(f"✓ {filename}")
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
            except KeyboardInterrupt:
                print("\n\nExiting...")
                break


def main():
    """Run the scenario modeler"""
    modeler = AudienceScenarioModeler()

    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        TARGET AUDIENCE SCENARIO MODELER                      ║
║                                                               ║
║     Test different target audiences and see how they         ║
║     affect brand names, pricing, channels, and revenue       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)

    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "--compare-all":
            modeler.compare_all_scenarios()
        elif sys.argv[1] == "--scenario":
            if len(sys.argv) > 2:
                scenario_key = sys.argv[2]
                result = modeler.analyze_scenario(scenario_key)
                modeler._print_scenario_detail(result)
            else:
                print("Usage: python audience_scenario_modeler.py --scenario <scenario_key>")
        else:
            print("Usage: python audience_scenario_modeler.py [--compare-all | --scenario <key>]")
    else:
        # Run interactive mode
        modeler.interactive_mode()


if __name__ == "__main__":
    main()
