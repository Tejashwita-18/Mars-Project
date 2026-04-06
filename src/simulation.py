def migration_analysis(mars_score, earth_score):
    if mars_score >= 8 and earth_score >= 8:
        return "Ancient Mars and Earth were both habitable — life transfer is scientifically plausible"
    
    elif mars_score >= 8 and earth_score < 8:
        return "Ancient Mars may have supported life before Earth — strong migration hypothesis"
    
    elif mars_score < 8 and earth_score >= 8:
        return "Earth is more suitable for life — migration less likely"
    
    else:
        return "Conditions on both planets were harsh — hypothesis weak"