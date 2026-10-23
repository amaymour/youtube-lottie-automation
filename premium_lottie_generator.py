#!/usr/bin/env python3
"""
Premium Lottie Animation Generator
High-grade 2D animations for YouTube content
"""

import json
import uuid
from typing import Dict, List, Any
from enum import Enum

class AnimationStyle(Enum):
    CINEMATIC_PREMIUM = "cinematic-premium"
    MINIMAL_CORPORATE = "minimal-corporate"
    LUXURY_PREMIUM = "luxury-premium"
    GAMING_ENERGETIC = "gaming-energetic"
    EDUCATIONAL_CLEAN = "educational-clean"
    TECH_STARTUP = "tech-startup"

class PremiumLottieGenerator:
    """Generate premium quality Lottie animations"""
    
    PREMIUM_COLORS = {
        "cinematic-premium": {
            "primary": [0.12, 0.12, 0.15, 1],
            "accent": [1, 0.65, 0.0, 1],
            "secondary": [0.2, 0.6, 1.0, 1],
            "background": [0.05, 0.05, 0.08, 1]
        },
        "luxury-premium": {
            "primary": [0.95, 0.85, 0.6, 1],
            "accent": [0.8, 0.2, 0.3, 1],
            "secondary": [0.4, 0.4, 0.45, 1],
            "background": [0.08, 0.07, 0.06, 1]
        },
        "minimal-corporate": {
            "primary": [0.15, 0.15, 0.15, 1],
            "accent": [0.0, 0.7, 0.9, 1],
            "secondary": [0.7, 0.7, 0.7, 1],
            "background": [0.98, 0.98, 0.98, 1]
        }
    }
    
    def __init__(self, style: str = "cinematic-premium"):
        self.style = style
        self.colors = self.PREMIUM_COLORS.get(style, self.PREMIUM_COLORS["cinematic-premium"])
    
    def generate_cinematic_intro(self, title: str, duration: float = 3.0) -> Dict[str, Any]:
        """Generate premium cinematic intro animation"""
        return {
            "v": "5.7.4",
            "fr": 60,  # 60 FPS for premium quality
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": f"Premium Intro: {title}",
            "ddd": 0,
            "assets": [],
            "layers": self._build_cinematic_intro_layers(title, duration)
        }
    
    def _build_cinematic_intro_layers(self, title: str, duration: float) -> List[Dict]:
        """Build premium cinematic intro layers"""
        layers = []
        
        # Background gradient layer
        layers.append({
            "ddd": 0,
            "ind": 1,
            "ty": 4,
            "nm": "Premium Background",
            "sr": 1,
            "ks": {
                "o": {"a": 0, "k": 100},
                "r": {"a": 0, "k": 0},
                "p": {"a": 0, "k": [960, 540, 0]},
                "a": {"a": 0, "k": [0, 0, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": self._create_premium_background()
        })
        
        # Animated shapes layer
        layers.append({
            "ddd": 0,
            "ind": 2,
            "ty": 4,
            "nm": "Premium Animated Shapes",
            "sr": 1,
            "ks": {
                "o": {"a": 1, "k": [
                    {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": 0, "s": [0]},
                    {"t": int(duration * 60 * 0.2), "s": [100]}
                ]},
                "r": {"a": 1, "k": [
                    {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": 0, "s": [0]},
                    {"t": int(duration * 60), "s": [360]}
                ]},
                "p": {"a": 0, "k": [960, 540, 0]},
                "a": {"a": 0, "k": [0, 0, 0]},
                "s": {"a": 1, "k": [
                    {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": 0, "s": [0, 0, 100]},
                    {"t": int(duration * 60 * 0.3), "s": [120, 120, 100]},
                    {"t": int(duration * 60), "s": [100, 100, 100]}
                ]}
            },
            "shapes": self._create_premium_shapes()
        })
        
        # Typography layer
        layers.append({
            "ddd": 0,
            "ind": 3,
            "ty": 5,  # Text layer
            "nm": "Premium Typography",
            "sr": 1,
            "ks": {
                "o": {"a": 1, "k": [
                    {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": 0, "s": [0]},
                    {"t": int(duration * 60 * 0.3), "s": [100]}
                ]},
                "r": {"a": 0, "k": 0},
                "p": {"a": 0, "k": [960, 600, 0]},
                "a": {"a": 0, "k": [0, 0, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "t": {
                "d": {"k": [{"s": {"t": title}, "t": 0}]},
                "f": {"a": 0, "k": "Montserrat-Bold"},
                "s": {"a": 0, "k": 120},
                "t": {"a": 0, "k": 0},
                "j": 1
            }
        })
        
        return layers
    
    def _create_premium_background(self) -> List[Dict]:
        """Create premium gradient background"""
        return [
            {
                "ty": "gr",
                "it": [
                    {
                        "ty": "sh",
                        "ks": {
                            "a": 0,
                            "k": {
                                "i": [[0,0], [0,0], [0,0], [0,0]],
                                "o": [[0,0], [0,0], [0,0], [0,0]],
                                "v": [[0,0], [1920,0], [1920,1080], [0,1080]],
                                "c": True
                            }
                        }
                    },
                    {
                        "ty": "gf",
                        "o": {"a": 0, "k": 100},
                        "s": {"a": 0, "k": 100},
                        "e": {"a": 0, "k": 0},
                        "t": 1,
                        "g": {
                            "p": {"a": 0, "k": [100, 100]},
                            "k": [
                                {"i": [0.25, 0.25], "o": [0.75, 0.75], "t": 0, "s": self.colors["background"]},
                                {"i": [0.25, 0.25], "o": [0.75, 0.75], "t": 1, "s": [0.1, 0.1, 0.15, 1]}
                            ]
                        }
                    }
                ]
            }
        ]
    
    def _create_premium_shapes(self) -> List[Dict]:
        """Create premium animated shapes with morphing"""
        return [
            {
                "ty": "gr",
                "it": [
                    {
                        "ty": "sh",
                        "ks": {
                            "a": 1,
                            "k": {
                                "i": [[0.833, 0.833], [0.833, 0.833], [0.833, 0.833]],
                                "o": [[0.167, 0.167], [0.167, 0.167], [0.167, 0.167]],
                                "v": [[-400, -300], [400, -300], [0, 400]],
                                "o": [0, 1],
                                "c": False
                            }
                        }
                    },
                    {
                        "ty": "fl",
                        "c": {"a": 0, "k": self.colors["accent"]},
                        "o": {"a": 0, "k": 80}
                    },
                    {
                        "ty": "tr",
                        "p": {"a": 0, "k": [0, 0]},
                        "a": {"a": 0, "k": [0, 0]}
                    }
                ]
            }
        ]
    
    def generate_kinetic_typography(self, text: str, duration: float = 5.0) -> Dict[str, Any]:
        """Generate premium kinetic typography animation"""
        return {
            "v": "5.7.4",
            "fr": 60,
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": f"Kinetic Typography: {text[:30]}",
            "ddd": 0,
            "assets": [],
            "layers": self._build_typography_layers(text, duration)
        }
    
    def _build_typography_layers(self, text: str, duration: float) -> List[Dict]:
        """Build kinetic typography layers"""
        word_count = len(text.split())
        layer_duration = int(duration * 60 / max(word_count, 1))
        
        layers = []
        for i, word in enumerate(text.split()[:20]):
            layers.append({
                "ddd": 0,
                "ind": i + 1,
                "ty": 5,
                "nm": f"Word {i+1}: {word}",
                "sr": 1,
                "ks": {
                    "o": {"a": 1, "k": [
                        {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": i * layer_duration, "s": [0]},
                        {"t": i * layer_duration + layer_duration // 3, "s": [100]},
                        {"t": (i + 1) * layer_duration, "s": [0]}
                    ]},
                    "r": {"a": 1, "k": [
                        {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": i * layer_duration, "s": [-90]},
                        {"t": i * layer_duration + layer_duration // 3, "s": [0]}
                    ]},
                    "p": {"a": 0, "k": [960, 540 + (i % 3 - 1) * 100, 0]},
                    "a": {"a": 0, "k": [0, 0, 0]},
                    "s": {"a": 1, "k": [
                        {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": i * layer_duration, "s": [80, 80, 100]},
                        {"t": i * layer_duration + layer_duration // 3, "s": [120, 120, 100]}
                    ]}
                },
                "t": {
                    "d": {"k": [{"s": {"t": word}, "t": 0}]},
                    "f": {"a": 0, "k": "Montserrat-Bold"},
                    "s": {"a": 0, "k": 96},
                    "t": {"a": 0, "k": 1},
                    "j": 1,
                    "tr": {"a": 0, "k": 20}
                }
            })
        
        return layers
    
    def generate_premium_transition(self, duration: float = 1.0) -> Dict[str, Any]:
        """Generate premium transition animation"""
        return {
            "v": "5.7.4",
            "fr": 60,
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": "Premium Transition",
            "ddd": 0,
            "assets": [],
            "layers": [
                {
                    "ddd": 0,
                    "ind": 1,
                    "ty": 4,
                    "nm": "Transition Layer",
                    "sr": 1,
                    "ks": {
                        "o": {"a": 1, "k": [
                            {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": 0, "s": [0]},
                            {"t": int(duration * 60 * 0.3), "s": [100]},
                            {"t": int(duration * 60 * 0.7), "s": [100]},
                            {"t": int(duration * 60), "s": [0]}
                        ]},
                        "r": {"a": 0, "k": 0},
                        "p": {"a": 0, "k": [960, 540, 0]},
                        "a": {"a": 0, "k": [0, 0, 0]},
                        "s": {"a": 1, "k": [
                            {"i": [0.833, 0.833, 0.833, 0.833], "o": [0.167, 0.167, 0.167, 0.167], "t": 0, "s": [0, 0, 100]},
                            {"t": int(duration * 60 * 0.5), "s": [150, 150, 100]},
                            {"t": int(duration * 60), "s": [300, 300, 100]}
                        ]}
                    },
                    "shapes": [
                        {
                            "ty": "gr",
                            "it": [
                                {
                                    "ty": "sh",
                                    "ks": {
                                        "a": 0,
                                        "k": {
                                            "i": [[0,0], [0,0]],
                                            "o": [[0,0], [0,0]],
                                            "v": [[960, 0], [960, 1080]],
                                            "c": True
                                        }
                                    }
                                },
                                {
                                    "ty": "fl",
                                    "c": {"a": 0, "k": self.colors["accent"]},
                                    "o": {"a": 0, "k": 100}
                                }
                            ]
                        }
                    ]
                }
            ]
        }

# Export function for MCP integration
def generate_premium_animation(scene_type: str, content: str, style: str = "cinematic-premium", duration: float = 5.0) -> Dict[str, Any]:
    """Generate premium animation based on scene type"""
    generator = PremiumLottieGenerator(style)
    
    if scene_type == "intro":
        return generator.generate_cinematic_intro(content, duration)
    elif scene_type == "typography":
        return generator.generate_kinetic_typography(content, duration)
    elif scene_type == "transition":
        return generator.generate_premium_transition(duration)
    else:
        return generator.generate_cinematic_intro(content, duration)

if __name__ == "__main__":
    # Test premium generation
    anim = generate_premium_animation("intro", "Premium Content", "cinematic-premium", 3.0)
    print(json.dumps(anim, indent=2)[:500])
