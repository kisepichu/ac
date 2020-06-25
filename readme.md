# 自分用競プロツールバージョン 2 (575)

- 自作 atcoder-tools もどきのリファクタリング
- 自分の環境で動けばよし！って感じなので wsl 以外だとバグるとかある

```bash
pip3 install pyyaml
pip3 install requests
pip3 install lxml
```
とかが必要で、ソースファイルと同じディレクトリに ac/ ごと入れて
```
python3 ac/ac.py
```
で実行

## 以下、めも

- コンテスト中にソースファイルを 1 個だけ使いまわしたい
- コンテスト(/ばちゃ)前に準備して、コンテスト中に短いコマンドで操作できるようにする
- エイリアス的なので`ac.py submit a`みたいのを`sub a`だけで書けるようにする: <br>
~/.bashrc
```
alias pre='python3 ac/ac.py init'
alias sub='python3 ac/ac.py submit'
alias cpy='python3 ac/ac.py copy'
alias clr='python3 ac/ac.py clear'
alias mksnip='python3 ac/ac.py make-snippet'
```
とかするとよさそう
- ↓の「整形して」の意味:
	+ `//sub-BOF`から`//sub-EOF`までのコードを評価する
	+ 長いテンプレートの上部に solve() 近辺を書き、submission 画面でスクロールせずに済むようにする
	+ ↑ではライブラリを貼った部分は省略し、ライブラリ名だけ表示する

## 仕様 予定

### 残す機能

- コンテスト(/ばちゃ)前:
	+ `init [url] -s [start_time]`: コンテストの準備
- コンテスト中:
	+ `submit [p]`: 整形して、問題 p のサンプルチェックをして、AC なら提出
		* `-c`: ステータスにかかわらず、yn で提出するか選択(答えが複数ある問題など)
		* `-f`: コンパイルせずに提出(abc_a など)(最近使ってないけど)(WA でるので)
	+ `copy`: 整形して、クリップボードにコピー(atcoder 以外のコンテストサイトなどで)
	+ `clear`: 全部消しテンプレートを貼る
- コンテスト以外
	+ `make-snippet`: [ライブラリ](https://tqkoh.github.io/library/)からソースコードを持ってきてスニペット化する (タイトル)[tab] と入力するとライブラリの中身が貼られるようにする(#include で提出されるときに埋め込まれるやつのほうがかっこいいが、ライブラリの中身をその場でいじりたいため)

### 対応するサイト

- AtCoder
	+ ばちゃ AtCoder Problems
	+ ばちゃ AVC
- CodeForces(追加)(できたら)
