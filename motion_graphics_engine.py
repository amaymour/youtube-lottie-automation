#!/usr/bin/env python3
"""
Premium Motion Graphics Engine for YouTube Automation
Advanced motion graphics generation using Lottie with premium effects
"""

import json
import math
from typing import Dict, List, Any, Tuple
from enum import Enum

class MotionGraphicType(Enum):
    SLIDE_REVEAL = "slide_reveal"
    WIPE_TRANSITION = "wipe_transition"
    PARTICLE_BURST = "particle_burst"
    MORPHING_SHAPES = "morphing_shapes"
    KINETIC_TYPING = "kinetic_typing"
    DATA_CHART_ANIMATED = "data_chart_animated"
    LOGO_REVEAL = "logo_reveal"
    LOWER_THIRD = "lower_third"
    CALL_TO_ACTION = "call_to_action"
    END_SCREEN = "end_screen"

class PremiumMotionGraphicsEngine:
    """Advanced motion graphics generation for premium YouTube content"""
    
    def __init__(self, style: str = "cinematic-premium"):
        self.style = style
        self.config = self._get_style_config(style)
    
    def _get_style_config(self, style: str) -> Dict:
        """Get premium style configuration"""
        configs = {
            "cinematic-premium": {
                "colors": {
                    "primary": [0.12, 0.12, 0.15, 1],
                    "accent": [1.0, 0.65, 0.0, 1],
                    "secondary": [0.2, 0.6, 1.0, 1],
                    "background": [0.05, 0.05, 0.08, 1]
                },
                "easing": "easeInOutCubic",
                "duration_multiplier": 1.2,
                "particle_count": 150
            },
            "luxury-premium": {
                "colors": {
                    "primary": [0.95, 0.85, 0.6, 1],
                    "accent": [0.8, 0.2, 0.3, 1],
                    "secondary": [0.4, 0.4, 0.45, 1],
                    "background": [0.08, 0.07, 0.06, 1]
                },
                "easing": "easeInOutQuart",
                "duration_multiplier": 1.5,
                "particle_count": 200
            }
        }
        return configs.get(style, configs["cinematic-premium"])
    
    def generate_slide_reveal(self, content: str, direction: str = "left", duration: float = 2.0) -> Dict[str, Any]:
        """Premium slide reveal motion graphic"""
        return {
            "v": "5.7.4",
            "fr": 60,
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": f"Slide Reveal: {content[:30]}",
            "layers": self._build_slide_layers(content, direction, duration)
        }
    
    def _build_slide_layers(self, content: str, direction: str, duration: float) -> List[Dict]:
        """Build slide reveal layers with premium effects"""
        layers = []
        
        # Background with gradient
        layers.append({
            "ind": 1,
            "ty": 4,
            "nm": "Premium BG",
            "ks": {
                "o": {"a": 0, "k": 100},
                "p": {"a": 0, "k": [960, 540, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": self._create_motion_bg()
        })
        
        # Sliding content panel
        offset = {"left": [-2000, 0], "right": [2000, 0], "up": [0, 2000], "down": [0, -2000]}[direction]
        
        layers.append({
            "ind": 2,
            "ty": 4,
            "nm": "Slide Panel",
            "ks": {
                "o": {"a": 0, "k": 100},
                "p": {"a": 0, "k": [960, 540, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": self._create_slide_panel(offset, duration)
        })
        
        # Content text with typewriter effect
        layers.append({
            "ind": 3,
            "ty": 5,
            "nm": "Slide Content",
            "ks": {
                "o": {"a": 1, "k": [
                    {"t": 0, "s": [0]},
                    {"t": int(duration * 60 * 0.3), "s": [100]}
                ]},
                "p": {"a": 0, "k": [960, 540, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "t": {
                "d": {"k": [{"s": {"t": content}, "t": 0}]},
                "f": {"a": 0, "k": "Montserrat-Bold"},
                "s": {"a": 0, "k": 84},
                "t": {"a": 0, "k": 0}
            }
        })
        
        return layers
    
    def generate_particle_burst(self, center: Tuple[float, float] = (960, 540), duration: float = 3.0) -> Dict[str, Any]:
        """Premium particle burst effect"""
        return {
            "v": "5.7.4",
            "fr": 60,
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": "Particle Burst",
            "layers": self._build_particle_layers(center, duration)
        }
    
    def _build_particle_layers(self, center: Tuple[float, float], duration: float) -> List[Dict]:
        """Build particle system layers"""
        layers = []
        particle_count = self.config["particle_count"]
        
        for i in range(min(particle_count, 50)):  # Limit for JSON size
            angle = (i / particle_count) * 2 * math.pi
            distance = 500 + (i % 10) * 20
            
            layers.append({
                "ind": i + 1,
                "ty": 4,
                "nm": f"Particle {i+1}",
                "ks": {
                    "o": {"a": 1, "k": [
                        {"t": 0, "s": [0]},
                        {"t": int(duration * 60 * 0.1), "s": [100]},
                        {"t": int(duration * 60), "s": [0]}
                    ]},
                    "p": {"a": 1, "k": [
                        {"t": 0, "s": [center[0], center[1], 0]},
                        {"t": int(duration * 60), "s": [
                            center[0] + math.cos(angle) * distance,
                            center[1] + math.sin(angle) * distance,
                            0
                        ]}
                    ]},
                    "s": {"a": 1, "k": [
                        {"t": 0, "s": [200, 200, 100]},
                        {"t": int(duration * 60 * 0.2), "s": [10, 10, 100]}
                    ]}
                },
                "shapes": self._create_particle_shape()
            })
        
        return layers
    
    def generate_logo_reveal(self, logo_text: str, duration: float = 4.0) -> Dict[str, Any]:
        """Premium logo reveal with multiple effects"""
        return {
            "v": "5.7.4",
            "fr": 60,
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": f"Logo Reveal: {logo_text}",
            "layers": self._build_logo_layers(logo_text, duration)
        }
    
    def _build_logo_layers(self, logo_text: str, duration: float) -> List[Dict]:
        """Build premium logo reveal"""
        layers = []
        
        # Glow background
        layers.append({
            "ind": 1,
            "ty": 4,
            "nm": "Glow Background",
            "ks": {
                "o": {"a": 1, "k": [
                    {"t": 0, "s": [0]},
                    {"t": int(duration * 60 * 0.5), "s": [100]},
                    {"t": int(duration * 60), "s": [0]}
                ]},
                "p": {"a": 0, "k": [960, 540, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": [{
                "ty": "gr",
                "it": [{
                    "ty": "sh",
                    "ks": {"a": 0, "k": {"v": [[900, 480], [1020, 480], [1020, 600], [900, 600]], "c": True}}
                }, {
                    "ty": "fl",
                    "c": {"a": 0, "k": self.config["colors"]["accent"]},
                    "o": {"a": 0, "k": 60}
                }]
            }]
        })
        
        # Logo text with scale and rotation
        layers.append({
            "ind": 2,
            "ty": 5,
            "nm": "Logo Text",
            "ks": {
                "o": {"a": 1, "k": [
                    {"t": 0, "s": [0]},
                    {"t": int(duration * 60 * 0.4), "s": [100]}
                ]},
                "p": {"a": 0, "k": [960, 540, 0]},
                "s": {"a": 1, "k": [
                    {"t": 0, "s": [0, 0, 100]},
                    {"t": int(duration * 60 * 0.3), "s": [120, 120, 100]},
                    {"t": int(duration * 60 * 0.4), "s": [100, 100, 100]}
                ]},
                "r": {"a": 1, "k": [
                    {"t": 0, "s": [-180]},
                    {"t": int(duration * 60 * 0.3), "s": [0]}
                ]}
            },
            "t": {
                "d": {"k": [{"s": {"t": logo_text}, "t": 0}]},
                "f": {"a": 0, "k": "Montserrat-Black"},
                "s": {"a": 0, "k": 120},
                "j": 1
            }
        })
        
        return layers
    
    def generate_lower_third(self, title: str, subtitle: str, duration: float = 5.0) -> Dict[str, Any]:
        """Premium lower third graphic"""
        return {
            "v": "5.7.4",
            "fr": 60,
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": f"Lower Third: {title}",
            "layers": self._build_lower_third_layers(title, subtitle, duration)
        }
    
    def _build_lower_third_layers(self, title: str, subtitle: str, duration: float) -> List[Dict]:
        """Build lower third animation"""
        layers = []
        
        # Sliding bar
        layers.append({
            "ind": 1,
            "ty": 4,
            "nm": "Lower Third Bar",
            "ks": {
                "o": {"a": 0, "k": 100},
                "p": {"a": 1, "k": [
                    {"t": 0, "s": [960, 1000, 0]},
                    {"t": int(duration * 60 * 0.2), "s": [960, 700, 0]}
                ]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": [{
                "ty": "gr",
                "it": [{
                    "ty": "sh",
                    "ks": {"a": 0, "k": {"v": [[-960, -50], [960, -50], [960, 50], [-960, 50]], "c": True}}
                }, {
                    "ty": "fl",
                    "c": {"a": 0, "k": self.config["colors"]["primary"]},
                    "o": {"a": 0, "k": 100}
                }, {
                    "ty": "st",
                    "c": {"a": 0, "k": self.config["colors"]["accent"]},
                    "o": {"a": 0, "k": 100},
                    "w": {"a": 0, "k": 4}
                }]
            }]
        })
        
        # Title text
        layers.append({
            "ind": 2,
            "ty": 5,
            "nm": "Lower Third Title",
            "ks": {
                "o": {"a": 1, "k": [
                    {"t": 0, "s": [0]},
                    {"t": int(duration * 60 * 0.3), "s": [100]}
                ]},
                "p": {"a": 0, "k": [200, 750, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "t": {
                "d": {"k": [{"s": {"t": title}, "t": 0}]},
                "f": {"a": 0, "k": "Montserrat-Bold"},
                "s": {"a": 0, "k": 72},
                "c": {"a": 0, "k": [1, 1, 1, 1]}
            }
        })
        
        # Subtitle text
        layers.append({
            "ind": 3,
            "ty": 5,
            "nm": "Lower Third Subtitle",
            "ks": {
                "o": {"a": 1, "k": [
                    {"t": 0, "s": [0]},
                    {"t": int(duration * 60 * 0.4), "s": [100]}
                ]},
                "p": {"a": 0, "k": [200, 820, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "t": {
                "d": {"k": [{"s": {"t": subtitle}, "t": 0}]},
                "f": {"a": 0, "k": "Montserrat-Regular"},
                "s": {"a": 0, "k": 48},
                "c": {"a": 0, "k": [0.8, 0.8, 0.8, 1]}
            }
        })
        
        return layers
    
    def generate_morphing_shapes(self, duration: float = 4.0) -> Dict[str, Any]:
        """Premium morphing shapes background"""
        return {
            "v": "5.7.4",
            "fr": 60,
            "ip": 0,
            "op": int(duration * 60),
            "w": 1920,
            "h": 1080,
            "nm": "Morphing Shapes",
            "layers": self._build_morphing_layers(duration)
        }
    
    def _build_morphing_layers(self, duration: float) -> List[Dict]:
        """Build morphing shapes animation"""
        shapes_data = [
            {"v": [[1920/2, 1080/3], [1920*3/4, 1080/2], [1920/4, 1080*2/3]]},
            {"v": [[1920/2, 1080/4], [1920*2/3, 1080*3/4], [1920/3, 1080*3/4]]},
            {"v": [[1920/3, 1080/3], [1920*2/3, 1080/3], [1920/2, 1080*2/3]]}
        ]
        
        layers = []
        
        for i, shape in enumerate(shapes_data):
            layers.append({
                "ind": i + 1,
                "ty": 4,
                "nm": f"Morph Shape {i+1}",
                "ks": {
                    "o": {"a": 1, "k": [
                        {"t": i * int(duration * 60 / 3), "s": [0]},
                        {"t": (i + 0.5) * int(duration * 60 / 3), "s": [80]},
                        {"t": (i + 1) * int(duration * 60 / 3), "s": [0]}
                    ]},
                    "p": {"a": 0, "k": [960, 540, 0]},
                    "s": {"a": 0, "k": [100, 100, 100]}
                },
                "shapes": [{
                    "ty": "gr",
                    "it": [{
                        "ty": "sh",
                        "ks": {
                            "a": 1,
                            "k": {
                                "v": shape["v"],
                                "i": [[0,0], [0,0], [0,0]],
                                "o": [[0,0], [0,0], [0,0]]
                            }
                        }
                    }, {
                        "ty": "fl",
                        "c": {"a": 0, "k": self.config["colors"]["accent"]},
                        "o": {"a": 0, "k": 60}
                    }]
                }]
            })
        
        return layers
    
    def _create_motion_bg(self) -> List[Dict]:
        """Create premium motion background"""
        return [{
            "ty": "gr",
            "it": [{
                "ty": "sh",
                "ks": {"a": 0, "k": {"v": [[0,0], [1920,0], [1920,1080], [0,1080]], "c": True}}
            }, {
                "ty": "gf",
                "g": {
                    "p": {"a": 0, "k": [50, 50]},
                    "k": [
                        {"t": 0, "s": self.config["colors"]["background"]},
                        {"t": 1, "s": [0.15, 0.15, 0.2, 1]}
                    ]
                }
            }]
        }]
    
    def _create_slide_panel(self, offset: List[int], duration: float) -> List[Dict]:
        """Create slide panel shape"""
        return [{
            "ty": "gr",
            "it": [{
                "ty": "sh",
                "ks": {
                    "a": 1,
                    "k": {
                        "v": [[0,0], [1920,0], [1920,1080], [0,1080]],
                        "p": [
                            {"t": 0, "s": offset},
                            {"t": int(duration * 60 * 0.2), "s": [0, 0]}
                        ]
                    }
                }
            }, {
                "ty": "fl",
                "c": {"a": 0, "k": self.config["colors"]["primary"]},
                "o": {"a": 0, "k": 90}
            }]
        }]
    
    def _create_particle_shape(self) -> List[Dict]:
        """Create particle shape"""
        return [{
            "ty": "gr",
            "it": [{
                "ty": "sh",
                "ks": {"a": 0, "k": {"v": [[-5,-5], [5,-5], [5,5], [-5,5]], "c": True}}
            }, {
                "ty": "fl",
                "c": {"a": 0, "k": self.config["colors"]["accent"]},
                "o": {"a": 0, "k": 100}
            }]
        }]

def generate_motion_graphic(motion_type: str, content: str = "", style: str = "cinematic-premium", duration: float = 3.0) -> Dict[str, Any]:
    """Generate premium motion graphic"""
    engine = PremiumMotionGraphicsEngine(style)
    
    generators = {
        'slide_reveal': lambda: engine.generate_slide_reveal(content, duration=duration),
        'particle_burst': lambda: engine.generate_particle_burst(duration=duration),
        'logo_reveal': lambda: engine.generate_logo_reveal(content or "LOGO", duration=duration),
        'lower_third': lambda: engine.generate_lower_third(content.split('|')[0] if '|' in content else content, 
                                                         content.split('|')[1] if '|' in content else "", duration=duration),
        'morphing_shapes': lambda: engine.generate_morphing_shapes(duration=duration),
        'wipe_transition': lambda: engine.generate_slide_reveal(content, direction="left", duration=duration)
    }
    
    generator = generators.get(motion_type, generators['slide_reveal'])
    return generator()

if __name__ == "__main__":
    # Test motion graphics
    mg = generate_motion_graphic('logo_reveal', 'PREMIUM', 'cinematic-premium', 4.0)
    print(json.dumps(mg, indent=2)[:500])
