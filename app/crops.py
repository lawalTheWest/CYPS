# app/crops.py

import os

def get_crop_data(crop_name):
    '''
        dynamically gets crop names
    '''
    if crops:
        crop_name = crops.get(crop_name.lower()) # Use lower() to ensure case-insensitive matching
        return crop_name
    # Check for the presence of the images in preferred order
    if os.path.exists(f"{crop_name}/{crop_name}_icon.png"):
        image = f"{crop_name}/{crop_name}_icon.png"
    elif os.path.exists(f"{crop_name}/{crop_name}_icon.jpeg"):
        image = f"{crop_name}/{crop_name}_icon.jpeg"
    else:
        image = f"{crop_name}/{crop_name}_icon.jpg"

# The template:
'''
crops = {
    "plant_1": {
        "Basic Ibformation": [
            "image": "plant_image.png",
            "common name: ",
            "Scientific name: ",
            "Family: ",
            "Origin and History: ",
        ],
        "description": [
            "Physical characteristics: ",
            "Varieties: "
        ],
        "uses": [
            "Human Consumption: ",
            "industrial Uses: "
        ],
        "nutritional_value": {
            "calories": 0,
            "carbohydrates": 0,
            "protein": 0,
            "fat": 0,
            "fiber": 0,
        },
        "growing_condition": {
            "temperature":"______",
            "Water content": "______",
            "Soil": [
                "Soil Type": "______",
                "Soil pH": "______",
            ]
        },
        "Cultivation practices": [
            "plant_on_farm_image_1": "plant.png",
            "Planting": "______cm",
            "crop_rotation": "________",
            "pests and dieseases": [
                "pest_image": plant_pest_1.png,
                "pests": ["____", "_____"],
                "image_of_diseased_plant": "diseased_plant.png"
                "dieseases": ["___", "____"]
            ],
            "fertilization": "_____"
        ],
        "Harvesting_and_storage": [
            "Harvesting Condition": "________",
            "post_harvesting handling": "_______",
            "Storage_condition": "______"
        ],
        "Yield_information": [
            "Average yield": "____ tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Comming Soon..."
        ],
        "Economic_importance": [
           "Market_demand": "________",
           "Economic_value": "________",
           "Trade": "______"
        ],
        "Research_innovation": [
            "Current_Reasearch": "________",
            "Breeding_programs": "________",
            "Technological_innovation": "",
        ],
        "Environmental_impact": [
            "Sustainability": "_________",
            "Ecological_Footprint": "________",
            "Conservation": "_______"
        ],
        "Case_study": [
            "Successful cultivation practices": "________",
            "Challenges and solutions": "________"
        ]
    },
}
'''

crops = {
        # The Wheati plant
        "wheat": {
            "Basic Information": {
                "image": "wheat/wheat_icon.png" if "wheat/wheat_icon.png" else "wheat/wheat_icon.jpg" if "wheat/wheat_icon.jpg" else "wheat/wheat_icon.jpeg",
                "common name": "Wheat",
                "Scientific name": "Triticum spp.",
                "Family": "Poaceae",
                "Origin and History": "Wheat is a cereal grain originally from the Levant region of the Near East and Ethiopian Highlands. It has been cultivated worldwide for thousands of years."
                },
            "description": {
                "Physical characteristics": "Wheat is a grass widely cultivated for its seed, a cereal grain which is a worldwide staple food. It grows to a height of 2 to 4 feet, with a central stem and long, slender leaves.",
                "Varieties": "Common varieties include hard red winter wheat, hard red spring wheat, soft red winter wheat, durum wheat, hard white wheat, and soft white wheat."
                },
            "uses": {
                "Human Consumption": "Wheat is primarily used for human consumption. It is processed into flour which is used to make bread, pasta, noodles, and various baked goods.",
                "industrial Uses": "Wheat is also used in the production of alcoholic beverages, animal feed, and biofuels."
                },
            "nutritional_value": {
                "calories": 327,
                "carbohydrates": 71.2,
                "protein": 12.6,
                "fat": 1.5,
                "fiber": 12.2
                },
            "growing_condition": {
                "temperature": "15-25°C (59-77°F)",
                "Water content": "300-900 mm annual rainfall",
                "Soil": {
                    "Soil Type": "Loamy soil with good drainage",
                    "Soil pH": "6.0-7.5"
                    }
                },
            "Cultivation practices": {
                "plant_on_farm_image_1": "wheat/wheat_plant.png" if "wheat/wheat_plant.png" else "wheat/wheat_plant.jpg" if "wheat/wheat_plant.jpg" else "wheat/wheat_plant.jpeg",
                "Planting": "2-4 cm depth",
                "crop_rotation": "Wheat is often rotated with legumes, maize, or other crops to maintain soil fertility and reduce pest pressure.",
                "pests and diseases": {
                    "pest_image": "wheat/wheat_pest.png" if "wheat/wheat_pest.png" else "wheat/wheat_pest.jpg" if "wheat/wheat_pest.jpg" else "wheat/wheat_pest.jpeg",
                    "pests": ["Aphids", "Wheat stem sawfly"],
                    "image_of_diseased_plant": "wheat/wheat_diseased.png" if "wheat/wheat_diseased.png" else "wheat/wheat_diseased.jpg" if "wheat/wheat_diseased.jpg" else "wheat/wheat_diseased.jpeg",
                    "diseases": ["Rust", "Powdery mildew", "Fusarium head blight"]
                    },
                "fertilization": "Requires balanced fertilization with nitrogen, phosphorus, and potassium."
                },
            "Harvesting_and_storage": {
                "Harvesting Condition": "Wheat is harvested when the grain moisture content is between 14-20%.",
                "post_harvesting handling": "Grains are threshed, cleaned, and dried to reduce moisture content to safe storage levels.",
                "Storage_condition": "Stored in cool, dry conditions with moisture content below 12% to prevent mold and pest infestation."
                },
            "Yield_information": {
                "Average yield": "3-4 tons per hectare",
                "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
                "Yield_prediction_models": "Coming Soon..."
                },
            "Economic_importance": {
                    "Market_demand": "High global demand as a staple food.",
                    "Economic_value": "Significant contributor to the global food supply and agricultural economy.",
                    "Trade": "Extensively traded on global markets, with major exporters including the USA, Canada, Russia, and Australia."
                    },
            "Research_innovation": {
                    "Current_Research": "Ongoing research into disease-resistant varieties and sustainable farming practices.",
                    "Breeding_programs": "Programs focused on developing high-yielding, drought-resistant, and disease-resistant wheat varieties.",
                    "Technological_innovation": "Advancements in precision agriculture and genetic modification."
                    },
            "Environmental_impact": {
                    "Sustainability": "Practices such as crop rotation and reduced tillage improve sustainability.",
                    "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce water and chemical usage are ongoing.",
                    "Conservation": "Efforts include maintaining soil health and biodiversity through sustainable farming practices."
                    },
            "Case_study": {
                    "Successful cultivation practices": "In areas like the North American plains, modern wheat varieties combined with advanced farming techniques have led to high productivity.",
                    "Challenges and solutions": "Climate change, pest resistance, and soil degradation are major challenges. Solutions include developing resilient crop varieties and adopting sustainable farming practices."
                    }
        },

        # The rice
        "rice": {
        "Basic Information": {
            "image": "rice/rice_icon.png" if "rice/rice_icon.png" else "rice/rice_icon.jpeg" if "rice/rice_icon.jpeg" else "rice/rice_icon.jpg",
            "common name": "Rice",
            "Scientific name": "Oryza sativa",
            "Family": "Poaceae",
            "Origin and History": "Rice is a cereal grain that is a staple food for a large part of the world's population. It is believed to have been first domesticated in the region of the Yangtze River basin in China."
        },
        "description": {
            "Physical characteristics": "Rice is a grass with a long, slender stem and narrow leaves. The plant grows to about 1 to 1.8 meters in height.",
            "Varieties": "Common varieties include japonica, indica, and glutinous rice."
        },
        "uses": {
            "Human Consumption": "Rice is primarily used for human consumption. It is cooked and eaten as a staple food in many cultures, and also used to make products such as rice flour, rice syrup, and rice bran oil.",
            "industrial Uses": "Rice is also used in the production of alcoholic beverages like sake, and in animal feed."
        },
        "nutritional_value": {
            "calories": 130,
            "carbohydrates": 28,
            "protein": 2.7,
            "fat": 0.3,
            "fiber": 0.4
        },
        "growing_condition": {
            "temperature": "20-37°C (68-99°F)",
            "Water content": "Requires 1500-2000 mm of water per crop cycle",
            "Soil": {
                "Soil Type": "Clay loam soil with good water retention",
                "Soil pH": "5.5-6.5"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "rice/rice_plant.png" if "rice/rice_plant.png" else "rice/rice_plant.jpeg" if "rice/rice_plant.jpeg" else "rice/rice_plant.jpg",
            "Planting": "Seeds are typically sown in nursery beds and later transplanted to flooded fields.",
            "crop_rotation": "Rice is often rotated with legumes or other crops to maintain soil fertility.",
            "pests and diseases": {
                "pest_image": "rice/rice_pest.png" if "rice/rice_pest.png" else "rice/rice_pest.jpeg" if "rice/rice_pest.jpeg" else "rice/rice_pest.jpg",
                "pests": ["Rice stem borer", "Rice leaf folder"],
                "image_of_diseased_plant": "rice/rice_diseased.png" if "rice/rice_diseased.png" else "rice/rice_diseased.jpeg" if "rice/rice_diseased.jpeg" else "rice/rice_diseased.jpg",
                "diseases": ["Rice blast", "Bacterial leaf blight"]
            },
            "fertilization": "Requires balanced fertilization with nitrogen, phosphorus, and potassium."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Rice is harvested when the grains are firm and have a moisture content of around 20%.",
            "post_harvesting handling": "Grains are threshed, cleaned, and dried to reduce moisture content to safe storage levels.",
            "Storage_condition": "Stored in cool, dry conditions with moisture content below 14% to prevent mold and pest infestation."
        },
        "Yield_information": {
            "Average yield": "4-6 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Water availability", "Pest pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High global demand as a staple food.",
            "Economic_value": "Significant contributor to the global food supply and agricultural economy.",
            "Trade": "Extensively traded on global markets, with major exporters including India, Thailand, Vietnam, and the USA."
        },
        "Research_innovation": {
            "Current_Research": "Ongoing research into high-yield and disease-resistant varieties.",
            "Breeding_programs": "Programs focused on developing high-yielding, drought-resistant, and disease-resistant rice varieties.",
            "Technological_innovation": "Advancements in precision agriculture and genetic modification."
        },
        "Environmental_impact": {
            "Sustainability": "Efforts to improve water use efficiency and reduce methane emissions.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce water and chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and biodiversity through sustainable farming practices."
        },
        "Case_study": {
            "Successful cultivation practices": "In regions like Southeast Asia, traditional and modern farming techniques have been combined to enhance productivity.",
            "Challenges and solutions": "Climate change, water scarcity, and pest resistance are major challenges. Solutions include developing resilient crop varieties and adopting sustainable farming practices."
        }
    },
}
