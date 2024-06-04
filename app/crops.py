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
        # The corn
        "corn": {
            "Basic Information": {
                "image": "corn/corn_icon.png" if "corn/corn_icon.png" else "corn/corn_icon.jpg" if "corn/corn_icon.jpg" else "corn/corn_icon.jpeg",
                "common name": "Corn",
                "Scientific name": "Zea mays",
                "Family": "Poaceae",
                "Origin and History": "Corn, also known as maize, is native to southern Mexico and Central America. It has been cultivated for over 9,000 years."
                },
            "description": {
                "Physical characteristics": "Corn is a tall, annual grass with a stout, erect stem and large, elongated leaves. It produces ears of grain enclosed in husks.",
                "Varieties": "Common varieties include Dent corn, Flint corn, Sweet corn, Popcorn, and Flour corn."
                },
            "uses": {
                "Human Consumption": "Corn is consumed as a vegetable (sweet corn), ground into flour (cornmeal), and used to make products like tortillas, corn syrup, and corn oil.",
                "industrial Uses": "Used in the production of animal feed, biofuels (ethanol), and as a raw material for various industrial products."
                },
            "nutritional_value": {
                "calories": 86,
                "carbohydrates": 19.02,
                "protein": 3.27,
                "fat": 1.35,
                "fiber": 2.7
                },
            "growing_condition": {
                "temperature": "18-24°C (64-75°F)",
                "Water content": "Regular watering, especially during the growing season, with an annual rainfall of 600-1,200 mm",
                "Soil": {
                    "Soil Type": "Well-drained, fertile loamy soil",
                    "Soil pH": "5.8-7.0"
                    }
                },
            "Cultivation practices": {
                "plant_on_farm_image_1": "corn/corn_plant.png" if "corn/corn_plant.png" else "corn/corn_plant.jpg" if "corn/corn_plant.jpg" else "corn/corn_plant.jpeg",
                "Planting": "Seeds are planted 2-5 cm deep, with spacing of 20-30 cm between plants and 60-90 cm between rows.",
                "crop_rotation": "Corn is often rotated with soybeans or legumes to improve soil health and reduce pest pressure.",
                "pests and diseases": {
                    "pest_image": "corn/corn_pest.png" if "corn/corn_pest.png" else "corn/corn_pest.jpg" if "corn/corn_pest.jpg" else "corn/corn_pest.jpeg",
                    "pests": ["Corn borers", "Corn earworms"],
                    "image_of_diseased_plant": "corn/corn_diseased.png" if "corn/corn_diseased.png" else "corn/corn_diseased.jpg" if "corn/corn_diseased.jpg" else "corn/corn_diseased.jpeg",
                    "diseases": ["Corn smut", "Leaf blight", "Maize dwarf mosaic virus"]
                    },
                "fertilization": "Corn benefits from balanced fertilization with nitrogen, phosphorus, and potassium."
                },
            "Harvesting_and_storage": {
                "Harvesting Condition": "Corn is harvested when the kernels reach maturity, usually 90-120 days after planting.",
                "post_harvesting handling": "Harvested ears should be handled carefully to avoid damage and stored in dry conditions.",
                "Storage condition": "Stored at 10-15°C with low humidity to prevent mold and pest infestation."
                },
            "Yield_information": {
                "Average yield": "8-12 tons per hectare",
                "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
                "Yield_prediction_models": "Coming Soon..."
                },
            "Economic_importance": {
                    "Market_demand": "High global demand for both human consumption and industrial uses.",
                    "Economic_value": "Significant contributor to the global food supply and agricultural economy.",
                    "Trade": "Extensively traded on global markets, with major exporters including the USA, Brazil, and Argentina."
                    },
            "Research_innovation": {
                    "Current_Research": "Ongoing research into improving yield, pest resistance, and drought tolerance.",
                    "Breeding_programs": "Programs focused on developing high-yielding, disease-resistant, and drought-tolerant varieties.",
                    "Technological_innovation": "Advancements in precision agriculture, genetic modification, and sustainable farming practices."
                    },
            "Environmental_impact": {
                    "Sustainability": "Practices such as crop rotation and reduced tillage improve sustainability.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce water and chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and biodiversity through sustainable farming practices."
            },
            "Case_study": {
                    "Successful cultivation practices": "In regions like the Midwest USA, modern cultivation techniques and favorable climate conditions have led to high yields.",
                    "Challenges and solutions": "Climate change, pest resistance, and soil degradation are major challenges. Solutions include developing resilient crop varieties and adopting sustainable farming practices."
                    },
            "Plantation Duration": "90-120 days from planting"
            },
            
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
            # the tomatoes
            "tomatoes": {
                    "Basic Information": {
                        "image": "tomatoes/tomatoes_icon.png" if "tomatoes/tomatoes_icon.png" else "tomatoes/tomatoes_icon.jpg" if "tomatoes/tomatoes_icon.jpg" else "tomatoes/tomatoes_icon.jpeg",
                        "common name": "Tomatoes",
                        "Scientific name": "Solanum lycopersicum",
                        "Family": "Solanaceae",
                        "Origin and History": "Tomatoes are native to western South America and Central America. They have been cultivated for thousands of years and are now grown worldwide."
                        },
                    "description": {
                        "Physical characteristics": "Tomatoes are herbaceous plants that typically grow to about 1-3 meters in height. They have a weak, woody stem that usually sprawls and requires support.",
                        "Varieties": "Common varieties include cherry tomatoes, beefsteak tomatoes, plum tomatoes, and heirloom tomatoes."
                        },
                    "uses": {
                        "Human Consumption": "Tomatoes are widely used in culinary applications. They are eaten raw, cooked, or processed into products like sauces, pastes, and juices.",
                        "industrial Uses": "Tomatoes are also used in the production of tomato-based products for the food industry."
                        },
                    "nutritional_value": {
                        "calories": 18,
                        "carbohydrates": 3.9,
            "protein": 0.9,
            "fat": 0.2,
            "fiber": 1.2
        },
        "growing_condition": {
            "temperature": "20-25°C (68-77°F)",
            "Water content": "Regular watering, especially during dry periods",
            "Soil": {
                "Soil Type": "Well-drained, fertile loamy soil",
                "Soil pH": "6.0-6.8"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "tomatoes/tomatoes_plant.png" if "tomatoes/tomatoes_plant.png" else "tomatoes/tomatoes_plant.jpg" if "tomatoes/tomatoes_plant.jpg" else "tomatoes/tomatoes_plant.jpeg",
            "Planting": "Seeds are planted 0.5-1 cm deep, with seedlings transplanted 6-8 weeks after germination.",
            "crop_rotation": "Tomatoes are often rotated with crops like beans and corn to prevent soil nutrient depletion.",
            "pests and diseases": {
                "pest_image": "tomatoes/tomatoes_pest.png" if "tomatoes/tomatoes_pest.png" else "tomatoes/tomatoes_pest.jpg" if "tomatoes/tomatoes_pest.jpg" else "tomatoes/tomatoes_pest.jpeg",
                "pests": ["Aphids", "Tomato hornworms"],
                "image_of_diseased_plant": "tomatoes/tomatoes_diseased.png" if "tomatoes/tomatoes_diseased.png" else "tomatoes/tomatoes_diseased.jpg" if "tomatoes/tomatoes_diseased.jpg" else "tomatoes/tomatoes_diseased.jpeg",
                "diseases": ["Blight", "Fusarium wilt", "Tomato mosaic virus"]
            },
            "fertilization": "Tomatoes require balanced fertilization with nitrogen, phosphorus, and potassium."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Tomatoes are harvested when they reach the desired color and firmness.",
            "post_harvesting handling": "Harvested tomatoes should be handled carefully to avoid bruising.",
            "Storage_condition": "Store in cool, dry conditions or refrigerated to extend shelf life."
        },
        "Yield_information": {
            "Average yield": "20-30 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High demand in both fresh and processed forms.",
            "Economic_value": "Significant contributor to agricultural income in many regions.",
            "Trade": "Extensively traded globally, with major producers including China, India, and the USA."
        },
        "Research_innovation": {
            "Current_Research": "Ongoing research into disease-resistant and higher-yielding varieties.",
            "Breeding_programs": "Programs focused on developing varieties with improved taste, shelf life, and resistance to pests.",
            "Technological_innovation": "Advancements in hydroponics and greenhouse farming."
        },
        "Environmental_impact": {
            "Sustainability": "Practices such as crop rotation and organic farming improve sustainability.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce water and chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and reducing pesticide use through integrated pest management."
        },
        "Case_study": {
            "Successful cultivation practices": "In areas like California, advanced irrigation and fertilization techniques have led to high productivity.",
            "Challenges and solutions": "Pest resistance and water scarcity are major challenges. Solutions include developing drought-resistant varieties and adopting efficient irrigation systems."
        },
        "Plantation Duration": "60-100 days from transplanting"
    },

    # the Beans
    "beans": {
        "Basic Information": {
            "image": "beans/beans_icon.png" if "beans/beans_icon.png" else "beans/beans_icon.jpg" if "beans/beans_icon.jpg" else "beans/beans_icon.jpeg",
            "common name": "Beans",
            "Scientific name": "Phaseolus spp.",
            "Family": "Fabaceae",
            "Origin and History": "Beans have been cultivated for thousands of years, originating from Central and South America."
        },
        "description": {
            "Physical characteristics": "Beans are herbaceous plants with climbing or bushy growth habits. They produce pods that contain edible seeds.",
            "Varieties": "Common varieties include kidney beans, black beans, pinto beans, and green beans."
        },
        "uses": {
            "Human Consumption": "Beans are a major source of protein and are consumed in various forms, including fresh, dried, and canned.",
            "industrial Uses": "Used in the production of food products and as animal feed."
        },
        "nutritional_value": {
            "calories": 347,
            "carbohydrates": 63,
            "protein": 21,
            "fat": 1.2,
            "fiber": 15.5
        },
        "growing_condition": {
            "temperature": "20-30°C (68-86°F)",
            "Water content": "Regular watering, especially during flowering and pod development",
            "Soil": {
                "Soil Type": "Well-drained, fertile soil",
                "Soil pH": "6.0-7.5"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "beans/beans_plant.png" if "beans/beans_plant.png" else "beans/beans_plant.jpg" if "beans/beans_plant.jpg" else "beans/beans_plant.jpeg",
            "Planting": "Seeds are planted 2-4 cm deep, with spacing depending on the variety (bush or pole).",
            "crop_rotation": "Beans are often rotated with cereals to enhance soil fertility.",
            "pests and diseases": {
                "pest_image": "beans/beans_pest.png" if "beans/beans_pest.png" else "beans/beans_pest.jpg" if "beans/beans_pest.jpg" else "beans/beans_pest.jpeg",
                "pests": ["Bean beetles", "Aphids"],
                "image_of_diseased_plant": "beans/beans_diseased.png" if "beans/beans_diseased.png" else "beans/beans_diseased.jpg" if "beans/beans_diseased.jpg" else "beans/beans_diseased.jpeg",
                "diseases": ["Rust", "Anthracnose", "Root rot"]
            },
            "fertilization": "Beans benefit from balanced fertilization, particularly nitrogen due to their nitrogen-fixing ability."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Beans are harvested when pods are fully developed and seeds have reached the desired size.",
            "post_harvesting handling": "Pods are threshed to extract seeds, which are then dried to safe moisture levels.",
            "Storage_condition": "Stored in cool, dry conditions to prevent mold and pest infestation."
        },
        "Yield_information": {
            "Average yield": "1-3 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High demand as a protein-rich food source.",
            "Economic_value": "Important crop for both subsistence and commercial farming.",
            "Trade": "Widely traded, with major producers including Brazil, the USA, and India."
        },
        "Research_innovation": {
            "Current_Research": "Research focuses on improving yield, disease resistance, and nutritional quality.",
            "Breeding_programs": "Programs aim to develop high-yielding, disease-resistant varieties.",
            "Technological_innovation": "Advancements in pest management and irrigation techniques."
        },
        "Environmental_impact": {
            "Sustainability": "Crop rotation and organic farming practices enhance sustainability.",
            "Ecological_Footprint": "Low ecological footprint; beans improve soil fertility through nitrogen fixation.",
            "Conservation": "Efforts include maintaining genetic diversity and promoting sustainable farming practices."
        },
        "Case_study": {
            "Successful cultivation practices": "In regions like the Midwest USA, crop rotation and integrated pest management have led to high yields.",
            "Challenges and solutions": "Pest resistance and climate variability are major challenges. Solutions include breeding resistant varieties and adopting climate-smart practices."
        },
        "Plantation Duration": "50-70 days from planting"
    },

    # Irish Potatoes
    "irish_potatoes": {
        "Basic Information": {
            "image": "irish_potatoes/irish_potatoes_icon.png" if "irish_potatoes/irish_potatoes_icon.png" else "irish_potatoes/irish_potatoes_icon.jpg" if "irish_potatoes/irish_potatoes_icon.jpg" else "irish_potatoes/irish_potatoes_icon.jpeg",
            "common name": "Irish Potatoes",
            "Scientific name": "Solanum tuberosum",
            "Family": "Solanaceae",
            "Origin and History": "Native to the Andean region of South America, potatoes have been cultivated for thousands of years."
        },
        "description": {
            "Physical characteristics": "Potato plants are herbaceous perennials that grow about 60 cm in height, with underground tubers that are the edible part.",
            "Varieties": "Common varieties include Russet, Yukon Gold, and Red Potatoes."
        },
        "uses": {
            "Human Consumption": "Potatoes are a staple food, consumed in various forms including boiled, baked, fried, and processed into products like chips and fries.",
            "industrial Uses": "Used in the production of alcohol, animal feed, and as a source of starch."
        },
        "nutritional_value": {
            "calories": 77,
            "carbohydrates": 17,
            "protein": 2,
            "fat": 0.1,
            "fiber": 2.2
        },
        "growing_condition": {
            "temperature": "15-20°C (59-68°F)",
            "Water content": "Regular watering, especially during tuber formation",
            "Soil": {
                "Soil Type": "Well-drained, fertile loamy soil",
                "Soil pH": "5.0-6.5"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "irish_potatoes/irish_potatoes_plant.png" if "irish_potatoes/irish_potatoes_plant.png" else "irish_potatoes/irish_potatoes_plant.jpg" if "irish_potatoes/irish_potatoes_plant.jpg" else "irish_potatoes/irish_potatoes_plant.jpeg",
            "Planting": "Seed potatoes are planted 5-10 cm deep, with spacing of 30-40 cm between plants.",
            "crop_rotation": "Potatoes are often rotated with cereals or legumes to maintain soil health.",
            "pests and diseases": {
                "pest_image": "irish_potatoes/irish_potatoes_pest.png" if "irish_potatoes/irish_potatoes_pest.png" else "irish_potatoes/irish_potatoes_pest.jpg" if "irish_potatoes/irish_potatoes_pest.jpg" else "irish_potatoes/irish_potatoes_pest.jpeg",
                "pests": ["Colorado potato beetle", "Aphids"],
                "image_of_diseased_plant": "irish_potatoes/irish_potatoes_diseased.png" if "irish_potatoes/irish_potatoes_diseased.png" else "irish_potatoes/irish_potatoes_diseased.jpg" if "irish_potatoes/irish_potatoes_diseased.jpg" else "irish_potatoes/irish_potatoes_diseased.jpeg",
                "diseases": ["Late blight", "Black scurf", "Potato virus Y"]
            },
            "fertilization": "Potatoes require balanced fertilization with nitrogen, phosphorus, and potassium."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Potatoes are harvested when the plants begin to die back and the tubers reach the desired size.",
            "post_harvesting handling": "Harvested tubers should be cured and stored in cool, dark conditions.",
            "Storage condition": "Stored at 4-7°C with high humidity to extend shelf life."
        },
        "Yield_information": {
            "Average yield": "20-30 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High demand as a staple food and processed product.",
            "Economic_value": "Significant contributor to the agricultural economy in many regions.",
            "Trade": "Widely traded, with major producers including China, India, and Russia."
        },
        "Research_innovation": {
            "Current_Research": "Research focuses on improving yield, disease resistance, and nutritional quality.",
            "Breeding_programs": "Programs aim to develop high-yielding, disease-resistant varieties.",
            "Technological_innovation": "Advancements in storage and pest management techniques."
        },
        "Environmental_impact": {
            "Sustainability": "Crop rotation and organic farming practices enhance sustainability.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and promoting sustainable farming practices."
        },
        "Case_study": {
            "Successful cultivation practices": "In regions like Idaho, USA, advanced irrigation and pest management techniques have led to high yields.",
            "Challenges and solutions": "Pest resistance and climate variability are major challenges. Solutions include developing resistant varieties and adopting efficient irrigation systems."
        },
        "Plantation Duration": "80-120 days from planting"
    },

    # The Sweet potatoes
    "sweet_potatoes": {
        "Basic Information": {
            "image": "sweet_potatoes/sweet_potatoes_icon.png" if "sweet_potatoes/sweet_potatoes_icon.png" else "sweet_potatoes/sweet_potatoes_icon.jpg" if "sweet_potatoes/sweet_potatoes_icon.jpg" else "sweet_potatoes/sweet_potatoes_icon.jpeg",
            "common name": "Sweet Potatoes",
            "Scientific name": "Ipomoea batatas",
            "Family": "Convolvulaceae",
            "Origin and History": "Sweet potatoes are native to Central and South America and have been cultivated for thousands of years."
        },
        "description": {
            "Physical characteristics": "Sweet potato plants are herbaceous vines with heart-shaped or lobed leaves and tuberous roots.",
            "Varieties": "Common varieties include Beauregard, Jewel, and Garnet."
        },
        "uses": {
            "Human Consumption": "Sweet potatoes are consumed boiled, baked, or fried and are used in various culinary dishes.",
            "industrial Uses": "Used in the production of starch, animal feed, and as a raw material for alcohol production."
        },
        "nutritional_value": {
            "calories": 86,
            "carbohydrates": 20.1,
            "protein": 1.6,
            "fat": 0.1,
            "fiber": 3.0
        },
        "growing_condition": {
            "temperature": "24-26°C (75-79°F)",
            "Water content": "Regular watering, especially during tuber formation",
            "Soil": {
                "Soil Type": "Well-drained, sandy loam soil",
                "Soil pH": "5.5-6.5"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "sweet_potatoes/sweet_potatoes_plant.png" if "sweet_potatoes/sweet_potatoes_plant.png" else "sweet_potatoes/sweet_potatoes_plant.jpg" if "sweet_potatoes/sweet_potatoes_plant.jpg" else "sweet_potatoes/sweet_potatoes_plant.jpeg",
            "Planting": "Slips are planted 10-15 cm deep, with spacing of 30-40 cm between plants.",
            "crop_rotation": "Sweet potatoes are often rotated with legumes or cereals to maintain soil health.",
            "pests and diseases": {
                "pest_image": "sweet_potatoes/sweet_potatoes_pest.png" if "sweet_potatoes/sweet_potatoes_pest.png" else "sweet_potatoes/sweet_potatoes_pest.jpg" if "sweet_potatoes/sweet_potatoes_pest.jpg" else "sweet_potatoes/sweet_potatoes_pest.jpeg",
                "pests": ["Sweet potato weevil", "Aphids"],
                "image_of_diseased_plant": "sweet_potatoes/sweet_potatoes_diseased.png" if "sweet_potatoes/sweet_potatoes_diseased.png" else "sweet_potatoes/sweet_potatoes_diseased.jpg" if "sweet_potatoes/sweet_potatoes_diseased.jpg" else "sweet_potatoes/sweet_potatoes_diseased.jpeg",
                "diseases": ["Black rot", "Fusarium wilt", "Root-knot nematodes"]
            },
            "fertilization": "Sweet potatoes benefit from balanced fertilization with nitrogen, phosphorus, and potassium."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Sweet potatoes are harvested when the tubers reach the desired size, usually 90-120 days after planting.",
            "post_harvesting handling": "Harvested tubers should be cured and stored in cool, dry conditions.",
            "Storage condition": "Stored at 13-15°C with high humidity to extend shelf life."
        },
        "Yield_information": {
            "Average yield": "10-25 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High demand as a nutritious food and processed product.",
            "Economic_value": "Important crop for both subsistence and commercial farming.",
            "Trade": "Widely traded, with major producers including China, Nigeria, and Uganda."
        },
        "Research_innovation": {
            "Current_Research": "Research focuses on improving yield, disease resistance, and nutritional quality.",
            "Breeding_programs": "Programs aim to develop high-yielding, disease-resistant varieties.",
            "Technological_innovation": "Advancements in storage and pest management techniques."
        },
        "Environmental_impact": {
            "Sustainability": "Crop rotation and organic farming practices enhance sustainability.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and promoting sustainable farming practices."
        },
        "Case_study": {
            "Successful cultivation practices": "In regions like North Carolina, USA, advanced cultivation techniques have led to high yields.",
            "Challenges and solutions": "Pest resistance and climate variability are major challenges. Solutions include developing resistant varieties and adopting efficient irrigation systems."
        },
        "Plantation Duration": "90-120 days from planting"
    },

    # The Yam
    "yam": {
        "Basic Information": {
            "image": "yam/yam_icon.png" if "yam/yam_icon.png" else "yam/yam_icon.jpg" if "yam/yam_icon.jpg" else "yam/yam_icon.jpeg",
            "common name": "Yam",
            "Scientific name": "Dioscorea spp.",
            "Family": "Dioscoreaceae",
            "Origin and History": "Yams are native to Africa and Asia and have been cultivated for thousands of years."
        },
        "description": {
            "Physical characteristics": "Yams are perennial herbaceous vines with heart-shaped leaves and large tuberous roots.",
            "Varieties": "Common varieties include White Yam, Yellow Yam, and Water Yam."
        },
        "uses": {
            "Human Consumption": "Yams are consumed boiled, fried, or roasted and used in various traditional dishes.",
            "industrial Uses": "Used in the production of starch, animal feed, and as a raw material for various industrial products."
        },
        "nutritional_value": {
            "calories": 118,
            "carbohydrates": 27.9,
            "protein": 1.5,
            "fat": 0.2,
            "fiber": 4.1
        },
        "growing_condition": {
            "temperature": "25-30°C (77-86°F)",
            "Water content": "Regular watering, especially during the growing season",
            "Soil": {
                "Soil Type": "Well-drained, fertile loamy soil",
                "Soil pH": "5.5-6.5"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "yam/yam_plant.png" if "yam/yam_plant.png" else "yam/yam_plant.jpg" if "yam/yam_plant.jpg" else "yam/yam_plant.jpeg",
            "Planting": "Seed yams or tuber pieces are planted 10-15 cm deep, with spacing of 1-2 meters between plants.",
            "crop_rotation": "Yams are often rotated with legumes or cereals to maintain soil health.",
            "pests and diseases": {
                "pest_image": "yam/yam_pest.png" if "yam/yam_pest.png" else "yam/yam_pest.jpg" if "yam/yam_pest.jpg" else "yam/yam_pest.jpeg",
                "pests": ["Yam beetles", "Nematodes"],
                "image_of_diseased_plant": "yam/yam_diseased.png" if "yam/yam_diseased.png" else "yam/yam_diseased.jpg" if "yam/yam_diseased.jpg" else "yam/yam_diseased.jpeg",
                "diseases": ["Anthracnose", "Yam mosaic virus", "Root rot"]
            },
            "fertilization": "Yams benefit from balanced fertilization with nitrogen, phosphorus, and potassium."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Yams are harvested when the vines begin to die back and the tubers reach the desired size.",
            "post_harvesting handling": "Harvested tubers should be handled carefully to avoid bruising and stored in cool, dry conditions.",
            "Storage condition": "Stored at 13-15°C with good ventilation to prevent spoilage."
        },
        "Yield_information": {
            "Average yield": "10-15 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High demand as a staple food and for industrial purposes.",
            "Economic_value": "Significant contributor to the agricultural economy, particularly in West Africa.",
            "Trade": "Widely traded, with major producers including Nigeria, Ghana, and Ivory Coast."
        },
        "Research_innovation": {
            "Current_Research": "Research focuses on improving yield, disease resistance, and nutritional quality.",
            "Breeding_programs": "Programs aim to develop high-yielding, disease-resistant varieties.",
            "Technological_innovation": "Advancements in pest management and storage techniques."
        },
        "Environmental_impact": {
            "Sustainability": "Crop rotation and organic farming practices enhance sustainability.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and promoting sustainable farming practices."
        },
        "Case_study": {
            "Successful cultivation practices": "In regions like Nigeria, traditional knowledge combined with modern techniques has led to high yields.",
            "Challenges and solutions": "Pest resistance and climate variability are major challenges. Solutions include developing resistant varieties and adopting efficient irrigation systems."
        },
        "Plantation Duration": "180-240 days from planting"
    },

    # The carrot
    "carrot": {
        "Basic Information": {
            "image": "carrot/carrot_icon.png" if "carrot/carrot_icon.png" else "carrot/carrot_icon.jpg" if "carrot/carrot_icon.jpg" else "carrot/carrot_icon.jpeg",
            "common name": "Carrot",
            "Scientific name": "Daucus carota",
            "Family": "Apiaceae",
            "Origin and History": "Carrots are believed to have originated in Persia (modern-day Iran and Afghanistan) and have been cultivated for over 1,000 years."
        },
        "description": {
            "Physical characteristics": "Carrots are root vegetables, usually orange in color, though purple, black, red, white, and yellow varieties exist. The plant has a rosette of finely divided leaves and a long, slender taproot.",
            "Varieties": "Common varieties include Imperator, Nantes, Danvers, Chantenay, and Miniature."
        },
        "uses": {
            "Human Consumption": "Carrots are consumed raw, cooked, or juiced and used in salads, soups, stews, and as a snack.",
            "industrial Uses": "Used in the production of carrot juice, baby food, and as an ingredient in processed foods."
        },
        "nutritional_value": {
            "calories": 41,
            "carbohydrates": 9.6,
            "protein": 0.9,
            "fat": 0.2,
            "fiber": 2.8
        },
        "growing_condition": {
            "temperature": "16-21°C (60-70°F)",
            "Water content": "Regular watering to keep the soil moist, especially during dry periods",
            "Soil": {
                "Soil Type": "Loose, well-drained sandy loam soil",
                "Soil pH": "6.0-6.8"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "carrot/carrot_plant.png" if "carrot/carrot_plant.png" else "carrot/carrot_plant.jpg" if "carrot/carrot_plant.jpg" else "carrot/carrot_plant.jpeg",
            "Planting": "Seeds are sown directly into the soil at a depth of 1-2 cm, with spacing of 5-8 cm between plants and 30-45 cm between rows.",
            "crop_rotation": "Carrots are often rotated with legumes or cereals to prevent soil depletion and reduce pest pressure.",
            "pests and diseases": {
                "pest_image": "carrot/carrot_pest.png" if "carrot/carrot_pest.png" else "carrot/carrot_pest.jpg" if "carrot/carrot_pest.jpg" else "carrot/carrot_pest.jpeg",
                "pests": ["Carrot rust fly", "Aphids"],
                "image_of_diseased_plant": "carrot/carrot_diseased.png" if "carrot/carrot_diseased.png" else "carrot/carrot_diseased.jpg" if "carrot/carrot_diseased.jpg" else "carrot/carrot_diseased.jpeg",
                "diseases": ["Alternaria leaf blight", "Powdery mildew", "Root-knot nematodes"]
            },
            "fertilization": "Carrots benefit from balanced fertilization with nitrogen, phosphorus, and potassium."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Carrots are harvested when they reach the desired size, usually 70-80 days after planting.",
            "post_harvesting handling": "Harvested carrots should be handled carefully to avoid bruising and stored in cool, dry conditions.",
            "Storage condition": "Stored at 0-4°C with high humidity to extend shelf life."
        },
        "Yield_information": {
            "Average yield": "25-40 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High demand as a nutritious vegetable and for processed products.",
            "Economic_value": "Important crop for both subsistence and commercial farming.",
            "Trade": "Widely traded, with major producers including China, the USA, and Russia."
        },
        "Research_innovation": {
            "Current_Research": "Research focuses on improving yield, disease resistance, and nutritional quality.",
            "Breeding_programs": "Programs aim to develop high-yielding, disease-resistant varieties.",
            "Technological_innovation": "Advancements in pest management and storage techniques."
        },
        "Environmental_impact": {
            "Sustainability": "Crop rotation and organic farming practices enhance sustainability.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and promoting sustainable farming practices."
        },
        "Case_study": {
            "Successful cultivation practices": "In regions like California, USA, modern cultivation techniques and favorable climate conditions have led to high yields.",
            "Challenges and solutions": "Pest resistance and climate variability are major challenges. Solutions include developing resistant varieties and adopting efficient irrigation systems."
        },
        "Plantation Duration": "70-80 days from planting"
    },

    # The pepper
    "pepper": {
        "Basic Information": {
            "image": "pepper/pepper_icon.png" if "pepper/pepper_icon.png" else "pepper/pepper_icon.jpg" if "pepper/pepper_icon.jpg" else "pepper/pepper_icon.jpeg",
            "common name": "Pepper",
            "Scientific name": "Capsicum spp.",
            "Family": "Solanaceae",
            "Origin and History": "Peppers are native to the Americas, specifically Mexico and Central America, and have been cultivated for thousands of years."
        },
        "description": {
            "Physical characteristics": "Peppers are flowering plants with a wide variety of fruit shapes, sizes, and colors, ranging from green, yellow, red, to purple.",
            "Varieties": "Common varieties include Bell Pepper, Jalapeno, Cayenne, Habanero, and Chili Pepper."
        },
        "uses": {
            "Human Consumption": "Peppers are consumed raw, cooked, or dried and used in a wide range of dishes, including salads, soups, sauces, and as a spice.",
            "industrial Uses": "Used in the production of sauces, spices, and as an ingredient in various processed foods."
        },
        "nutritional_value": {
            "calories": 40,
            "carbohydrates": 9,
            "protein": 1.8,
            "fat": 0.4,
            "fiber": 2.1
        },
        "growing_condition": {
            "temperature": "20-30°C (68-86°F)",
            "Water content": "Regular watering to keep the soil consistently moist",
            "Soil": {
                "Soil Type": "Well-drained, fertile loamy soil",
                "Soil pH": "6.0-7.0"
            }
        },
        "Cultivation practices": {
            "plant_on_farm_image_1": "pepper/pepper_plant.png" if "pepper/pepper_plant.png" else "pepper/pepper_plant.jpg" if "pepper/pepper_plant.jpg" else "pepper/pepper_plant.jpeg",
            "Planting": "Seeds are sown indoors 8-10 weeks before the last frost date and transplanted outdoors after the risk of frost has passed. Spacing of 45-60 cm between plants and 60-90 cm between rows.",
            "crop_rotation": "Peppers are often rotated with legumes or cereals to prevent soil depletion and reduce pest pressure.",
            "pests and diseases": {
                "pest_image": "pepper/pepper_pest.png" if "pepper/pepper_pest.png" else "pepper/pepper_pest.jpg" if "pepper/pepper_pest.jpg" else "pepper/pepper_pest.jpeg",
                "pests": ["Aphids", "Spider mites"],
                "image_of_diseased_plant": "pepper/pepper_diseased.png" if "pepper/pepper_diseased.png" else "pepper/pepper_diseased.jpg" if "pepper/pepper_diseased.jpg" else "pepper/pepper_diseased.jpeg",
                "diseases": ["Bacterial spot", "Anthracnose", "Pepper mosaic virus"]
            },
            "fertilization": "Peppers benefit from balanced fertilization with nitrogen, phosphorus, and potassium."
        },
        "Harvesting_and_storage": {
            "Harvesting Condition": "Peppers are harvested when they reach the desired size and color, usually 60-90 days after planting.",
            "post_harvesting handling": "Harvested peppers should be handled carefully to avoid bruising and stored in cool, dry conditions.",
            "Storage condition": "Stored at 7-10°C with moderate humidity to extend shelf life."
        },
        "Yield_information": {
            "Average yield": "10-25 tons per hectare",
            "Factors affecting yield": ["Soil Fertility", "Weather conditions", "Pests pressure and diseases"],
            "Yield_prediction_models": "Coming Soon..."
        },
        "Economic_importance": {
            "Market_demand": "High demand as a fresh vegetable and for processed products.",
            "Economic_value": "Important crop for both subsistence and commercial farming.",
            "Trade": "Widely traded, with major producers including China, Mexico, and Turkey."
        },
        "Research_innovation": {
            "Current_Research": "Research focuses on improving yield, disease resistance, and nutritional quality.",
            "Breeding_programs": "Programs aim to develop high-yielding, disease-resistant varieties.",
            "Technological_innovation": "Advancements in pest management and storage techniques."
        },
        "Environmental_impact": {
            "Sustainability": "Crop rotation and organic farming practices enhance sustainability.",
            "Ecological_Footprint": "Moderate ecological footprint; efforts to reduce chemical usage are ongoing.",
            "Conservation": "Efforts include maintaining soil health and promoting sustainable farming practices."
        },
        "Case_study": {
            "Successful cultivation practices": "In regions like California, USA, modern cultivation techniques and favorable climate conditions have led to high yields.",
            "Challenges and solutions": "Pest resistance and climate variability are major challenges. Solutions include developing resistant varieties and adopting efficient irrigation systems."
        },
        "Plantation Duration": "60-90 days from planting"
    },

}
