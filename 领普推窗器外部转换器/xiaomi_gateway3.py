from custom_components.xiaomi_gateway3.core.converters.devices import *

DEVICES = [{
    10939: ["Linptech", "Intelligent Sliding Window Driver WD1", "WD1"],
    "spec": [
        MapConv("motor", "cover", mi="2.p.1", map={
            0: "stop", 1: "open", 2: "close"
        }),
        Converter("target_position", mi="2.p.3"),
        CurtainPosConv("position", mi="2.p.2", parent="motor"),
        Converter("battery", "sensor", mi="3.p.1"),  # percent
    ],
    "ttl": "7d",
}] + DEVICES