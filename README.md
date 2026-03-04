[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/watanabe3tipapa/notion-ollama-webui)

# Notion + Ollama Web UI

FastAPI + HTMLベースのWeb UIからNotionページに指示出しするツール

## 特徴

- WebブラウザからNotionページにアクセス
- Ollamaで要約・翻訳・QAなど 
- 簡単セットアップ
- 他のマシンへ容易移植

## クイックスタート

```bash
# 1. リポジトリをクローン
git clone https://github.com/watanabe3tipapa/notion-ollama-webui.git
cd notion-ollama-webui

# 2. 依存関係をインストール
uv sync

# 3. 環境変数を設定
cp .env.example .env
# .envファイルを編集（NOTION_API_KEYを入力）

# 4. サーバーを起動
uv run uvicorn main:app --reload

# 5. ブラウザで開く
http://localhost:8000
```

## 詳細ドキュメント

- [USAGE.html](https://watanabe3tipapa.github.io/notion-ollama-webui/docs/USAGE.html) - 詳しい使い方

## 必要な環境

- Python 3.13+
- [uv](https://github.com/astral-sh/uv)
- [Ollama](https://ollama.com/)（ローカルで起動中）
- Notion APIキー

## ライセンス

MIT
