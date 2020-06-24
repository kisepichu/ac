# 自分用競プロツール(つくりかけ)

- atcoder-tools は神なのでそれをつかおう
- ps1 で長く使いながら機能追加してったらやりすぎてクソコードになったので最低限以外消す + python でリファクタリング
- 自分の環境で動けばヨシ！
```bash
pip3 install pyyaml
pip3 install requests
pip3 install lxml
```
とかが必要

## 以下、めも

- コンテスト中にソースファイルを 1 個だけ使いまわしたい
- コンテスト(/ばちゃ)前に準備して、コンテスト/(ばちゃ)中に短いコマンドで操作できるようにする
- エイリアス的なので`ac.py submit x`みたいのを`sub x`だけで書けるようにする: \\
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
	+ `init`: コンテスト(/ばちゃ)開始と同時に、用意されたコンテスト(/ばちゃ)情報にある問題のテストケースをダウンロードする
- コンテスト(/ばちゃ)中:
	+ `submit x`: 整形して、問題 x のサンプルチェックをして、AC なら提出 オプション:
		* `-c`: ステータスにかかわらず、yn で提出するか選択(答えが複数ある問題など)
		* `-f`: コンパイルせずに提出(abc_a など)(最近使ってないけど)(WA でるので)
	+ `copy`: 整形して、クリップボードにコピー(atcoder 以外のコンテストサイトなどで)
	+ `clear`: 全部消しテンプレートを貼る
- コンテスト(/ばちゃ)以外
	+ `make-snippet`: [ライブラリ](https://tqkoh.github.io/library/)からソースコードを持ってきてスニペット化する (タイトル)[tab] と入力するとライブラリの中身が貼られるようにする(#include で提出されるときに埋め込まれるやつのほうがかっこいいが、ライブラリの中身をその場でいじりたいため)

### 対応するサイト

- AtCoder
	+ ばちゃ AtCoder Problems
	+ ばちゃ AVC
- CodeForces(追加)(できたら)
