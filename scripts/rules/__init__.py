from . import almanac_agent, llm_agent, macro_agent, technical_agent

REGISTRY = {
    "almanac_agent": almanac_agent.RULES,
    "llm_agent": llm_agent.RULES,
    "macro_agent": macro_agent.RULES,
    "technical_agent": technical_agent.RULES,
}
