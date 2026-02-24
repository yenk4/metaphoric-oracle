"""Maps user's mood answers to a FLUX image prompt."""

WEATHER_MAP = {
    "Stormy": "dramatic stormy",
    "Foggy": "ethereal misty",
    "Sunny": "radiant golden",
    "Rainy": "melancholic rainy",
    "Blizzard": "icy cold",
}

ANIMAL_MAP = {
    "Wolf": "fierce solitary wolf energy",
    "Cat": "mysterious graceful cat energy",
    "Deer": "gentle shy deer energy",
    "Raven": "shadowy dark raven energy",
    "Fox": "cunning clever fox energy",
    "Owl": "wise ancient owl energy",
}

COLOR_MAP = {
    "Deep blue": "cool blue tones",
    "Crimson": "warm crimson red",
    "Violet": "purple violet haze",
    "Gold": "golden warm light",
    "Silver": "moonlit silver",
    "Forest green": "earthy deep green",
}

ELEMENT_MAP = {
    "Fire": "blazing fire",
    "Water": "fluid flowing water",
    "Earth": "grounded earth",
    "Air": "airy light wind",
    "Void": "dark ethereal void",
}

LANDSCAPE_MAP = {
    "Ocean": "vast open ocean",
    "Forest": "lush dense forest",
    "Desert": "arid vast desert",
    "City": "urban neon city",
    "Mountain": "towering rocky peaks",
    "Cave": "hidden cave depth",
}


def build_prompt(weather: str, animal: str, color: str, element: str, landscape: str) -> str:
    weather_term = WEATHER_MAP.get(weather, "dramatic")
    animal_term = ANIMAL_MAP.get(animal, "mysterious")
    color_term = COLOR_MAP.get(color, "rich tones")
    element_term = ELEMENT_MAP.get(element, "elemental")
    landscape_term = LANDSCAPE_MAP.get(landscape, "vast")

    prompt = (
        f"a dramatic fantasy portrait, {animal_term}, {weather_term} atmosphere, "
        f"{color_term} palette, {landscape_term} background, {element_term} energy, "
        f"cinematic lighting, painterly style, high detail, fantasy art, "
        f"soft focus background, face close-up, expressive eyes"
    )
    return prompt
