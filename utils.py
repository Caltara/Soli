def suggest_hashtags(topic):
    base_tags = {
        "marketing": ["#DigitalMarketing", "#GrowthHacking", "#MarketingTips"],
        "fitness": ["#FitLife", "#GymMotivation", "#HealthyHabits"],
        "ai": ["#ArtificialIntelligence", "#TechTrends", "#AItools"],
        "real estate": ["#RealtorLife", "#HomeBuying", "#RealEstateTips"],
        "default": ["#Inspiration", "#SocialMedia", "#ContentCreator"]
    }

    topic = topic.lower()
    for key in base_tags:
        if key in topic:
            return base_tags[key]

    return base_tags["default"]
