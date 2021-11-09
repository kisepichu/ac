# **自分用**競プロツールバージョン 2 (575) めも

- 自作 atcoder-tools もどきのリファクタリング
- 自分の環境で動けばいい wsl1

```bash
pip3 install pyyaml
pip3 install requests
pip3 install lxml
...
```
とかが必要で、ソースファイルと同じディレクトリに ac/ac/ を入れて
```
python3 ac/ac.py
```
で実行

- コンテスト中にソースファイルを 1 個だけ使いまわしたい
- コンテスト(/ばちゃ)前に準備して、コンテスト中に短いコマンドで操作できるようにしたい
- エイリアス的なので`ac.py submit a`みたいのを`sub a`だけで書けるようにする: <br>
~/.bashrc
```
alias pre='python3 ac/ac.py init'
alias sub='python3 ac/ac.py submit'
alias cpy='python3 ac/ac.py copy'
alias clr='python3 ac/ac.py clear'
alias mksnip='python3 ac/ac.py make-snippets'
```
とかするとよさそう
- ↓の「整形して」の意味:
	+ `//sub-BOF`から`//sub-EOF`までのコードを評価する
	+ 長いテンプレートの上部に solve() 近辺を書き、submission 画面でスクロールせずに済むようにする
	+ ↑ではライブラリを貼った部分は省略し、ライブラリ名だけ表示する

## 仕様 予定

+ :heavy_check_mark: `init [url]`: コンテストの準備
例 `python3 ac/ac.py init https://atcoder.jp/contests/abc130`

+ :heavy_check_mark: `submit [p]`: 整形して、問題 p のサンプルチェックをして、AC なら提出
	* `-c`: ステータスにかかわらず、yn で提出するか選択(正答が複数ある問題など)
	* `-f`: コンパイルせずに提出
例 `python3 ac/ac.py submit b`

+ :heavy_check_mark: `copy`: 整形して、クリップボードにコピー(atcoder 以外のコンテストサイトなどで)
+ :heavy_check_mark: `clear`: 全部消しテンプレートを貼る
+ :heavy_check_mark: `make-snippets`: [ライブラリ](https://tqkoh.github.io/library/)からソースコードを持ってきてスニペット化する (タイトル)[tab] と入力するとライブラリの中身が貼られるようにする(#include で提出されるときに埋め込まれるやつのほうがかっこいいが、ライブラリの中身をその場でいじりたいため)
+ :x: `generate [p]`: 入力を生成するアレ
+ :x: `test-library?`: ライブラリのテスト(個別)の書き途中用に.test.cpp の個別実行・確認

## 対応するサイト

- :heavy_minus_sign: AtCoder
  + :heavy_check_mark: 本家
  + ばちゃ AtCoder Problems
  + ~~ばちゃ AVC~~
- :x: CodeForcesできたら)
- :x: AOJ(できたら)
- :x: yosupo judge(できたら)
