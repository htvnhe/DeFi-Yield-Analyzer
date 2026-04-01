# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class DeFiYieldAnalyzer(gl.Contract):
    has_scanned: bool
    best_protocol: str
    best_apy: str
    risk_level: str
    scan_url: str

    def __init__(self, scan_url: str):
        self.has_scanned = False
        self.best_protocol = "unknown"
        self.best_apy = "0"
        self.risk_level = "MEDIUM"
        self.scan_url = scan_url

    @gl.public.write
    def analyze_yields(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            response = gl.nondet.web.render(self.scan_url, mode="text")
            print(response)

            task = f"""You are a DeFi yield analyst.
            Analyze the following DeFi data to find the best yield opportunities:
            {response[:2000]}

            Respond with the following JSON format:
            {{
                "best_protocol": str,
                "best_apy": str,
                "risk_level": str,
                "summary": str
            }}
            best_protocol: name of the protocol with best risk-adjusted yield.
            best_apy: the APY percentage as a string number.
            risk_level: one of LOW, MEDIUM, HIGH, EXTREME.
            summary: one sentence about current DeFi yield landscape.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.best_protocol = result_json["best_protocol"]
        self.best_apy = str(result_json["best_apy"])
        self.risk_level = result_json["risk_level"]

        return result_json
