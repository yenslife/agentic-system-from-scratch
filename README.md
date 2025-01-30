# Build an Agentic System from Scratch

這是一個用來檢視自身對 LLM-based Agent 理解的練習用專案

本專案受到 ihower 大大的[淺談 LLM-based AI Agents 應用開發](https://ihower.tw/presentation/ihower-agents-202412.pdf)以及 [Dify](https://github.com/langgenius/dify) 很多啟發，感謝他們的貢獻！

## TODOs

目前的實作，Agent 無法從 JSON Schema 得到工具的參數 description，可能可以透過定義 tools 的 docstring 來解決；Agent run 的 debug 有改善的空間