# **自分用**競プロツールバージョン 2 (575) めも

- 自己満 atcoder-tools もどき
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

## やりたいこと

- コンテスト中にソースファイルを 1 個だけ使いまわす
- コンテスト(/ばちゃ)前に準備して、コンテスト中に短いコマンドで操作できるようにする
- 提出コマンドでは整形してから出す:
	+ `//sub-BOF`から`//sub-EOF`までのコードを評価する
	+ 提出ページの一番上に本文が来るようにする 長いテンプレートではなく
	+ ライブラリを貼った部分は省略し、ライブラリ名だけ表示する
- 短く書く: <br>
~/.bashrc
```
alias pre='python3 ac/ac.py init'
alias sub='python3 ac/ac.py submit'
alias cpy='python3 ac/ac.py copy'
alias clr='python3 ac/ac.py clear'
alias mksnip='python3 ac/ac.py make-snippets'
```
- ライブラリへの追加を簡単にできるようにしたい

## 仕様 予定

+ :heavy_check_mark: `init [url]`: コンテストの準備
例 `python3 ac/ac.py init https://atcoder.jp/contests/abc130`

+ :heavy_check_mark: `submit [p]`: 整形して、問題 p のサンプルチェックをして、AC なら提出
	* `-c`: ステータスにかかわらず、yn で提出するか選択(正答が複数ある問題など)
	* `-f`: コンパイルせずに提出
例 `python3 ac/ac.py submit b`

+ :heavy_check_mark: `copy`: 整形して、クリップボードにコピー(atcoder 以外のコンテストサイトなどで)
+ :heavy_check_mark: `clear`: 全部消しテンプレートを貼る
+ :heavy_check_mark: `make-snippets`: [ライブラリ](https://tqkoh.github.io/library/)からソースコードを持ってきてスニペット化する (タイトル)[tab] と入力するとライブラリの中身が貼られるようにする(#include で提出されるときに埋め込まれるやつのほうがかっこいいが、ライブラリの中身をその場でいじりたいため) <- いじらないように変えるか悩む
+ :x: `generate [p]`: 入力を生成するアレ

## 対応するサイト

- :heavy_minus_sign: AtCoder
  + :heavy_check_mark: 本家
  + :x: ばちゃ AtCoder Problems
  + :x: ~~ばちゃ AVC~~
- :x: CodeForcesできたら)
