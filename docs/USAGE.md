# Notion + Ollama Web UI 使用方法

## 準備

### 1. Notion APIキー取得
1. [notion.so/developers](https://www.notion.so/developers) にアクセス
2. 「New integration」をクリック
3. 名前を入力（例: `notion-ollama-webui`）
4. 「Capabilities」で Full Access を選択
5. 保存後、Secretキーをコピー

### 2. 環境変数設定
```bash
cp .env.example .env
```

`.env`ファイルを編集：
```
NOTION_API_KEY=secret_xxxxx（取得したAPIキー）
```

## 実行

### 1. 依存関係をインストール
```bash
uv sync
```

### 2. サーバーを起動
```bash
uv run uvicorn main:app --reload
```

### 3. ブラウザで開く
```
http://localhost:8000
```

## 使い方

1. **Notion ページID** を入力
   - 例: `https://notion.so/page-name-abc123def456` → `abc123def456`

2. **プロンプト** を選択
   - 要約
   - 英語に翻訳
   - キーワード抽出
   - Q&A

3. 「実行」ボタンをクリック

## カスタマイズ

### モデル変更
`main.py` のこの部分：
```python
response = chat('llama3.2', messages=[...])
```
`llama3.2` を他のモデル名に置換

### プロンプト追加
`templates/index.html` の `<select>` タグに选项を追加

## 他のマシンへ移植する場合

### 準備（現在のパソコンで）
テスト成功後、以下のコマンドで依存関係を固定：
```bash
uv sync
```
これにより `uv.lock` が更新され、相手の環境で同じバージョンが使われる

### 移植手順（相手のマシンで）
1. プロジェクトフォルダを丸ごとコピー
2. ターミナルでフォルダに移動
3. 以下を実行：
```bash
uv sync
```
4. `.env` ファイルを作成し、APIキーを設定

### 必要な環境
- Python 3.13+
- uv
- Ollama（ローカルで起動中）
- Notion APIキー

## Ollamaのセットアップ

### 1. Ollamaをインストール
Mac/Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Ollamaを起動
```bash
ollama serve
```

### 3. モデルをダウンロード
```bash
ollama pull llama3.2
```

### 4. 確認
```bash
ollama list
```

## トラブルシューティング

### Ollamaが起動しない
```bash
# ポート11434が使用中か確認
lsof -i :11434
```

### サーバーが起動しない
```bash
# ポート8000が使用中か確認
lsof -i :8000
```
