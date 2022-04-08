[![Test generate](https://github.com/tqkoh/ac/actions/workflows/test_generate.yaml/badge.svg)](https://github.com/tqkoh/ac/actions/workflows/test_generate.yaml)
[![Tqk](https://img.shields.io/endpoint?url=https%3A%2F%2Fatcoder-badges.now.sh%2Fapi%2Fatcoder%2Fjson%2FTqk)](https://atcoder.jp/users/Tqk)
[![Tqk](https://img.shields.io/endpoint?url=https%3A%2F%2Fatcoder-badges.now.sh%2Fapi%2Fcodeforces%2Fjson%2FTqk)](https://codeforces.com/profile/Tqk)

# **自分用**競プロツール備忘録(575)

- atcoder-tools 自分用
- 常に作りかけ
- 自分の環境で動けばいい wsl1 Ubuntu 18.04 LTS

## インストール
```bash
pip3 install -r requirements.txt
```
- タリンかも

## 実行
```
python3 ac/ac.py
```

## やりたいこと

- コンテスト中にソースファイルを 1 個だけ使いまわす
- コンテスト中に短いコマンドでテスト、提出などの操作をできるようにする
- 各コマンドでは整形してから処理する:
	- `//sub-BOF`から`//sub-EOF`までを抜き出す
	- 提出ページの一番上に本文(ダミー)が来るようにする 長いテンプレートではなく
	- ライブラリを貼った部分は省略し、ライブラリ名だけ表示する
- 短く書く: <br>
~/.bashrc に追加するなど
```
alias pre='python3 ac/ac.py init'
alias sub='python3 ac/ac.py submit'
alias cpy='python3 ac/ac.py copy'
alias tpy='python3 ac/ac.py case copy'
alias clr='python3 ac/ac.py clear'
alias cmp='python3 ac/ac.py compile'
alias run='python3 ac/ac.py run'
alias g='python3 ac/ac.py generate'
alias mksnip='python3 ac/ac.py make-snippets'
```
- ライブラリへの追加を簡単にできるようにしたい

## コマンド

- コンテストに出るとき、この順に実行する
- p は指定しなければ前回実行時の問題番号が使われる(全コマンド共通)<br>なので基本 `generate` のみで p を指定する
- 実装済み: :heavy_check_mark:、未実装: :x:

---

- :heavy_check_mark: `init [url]`: コンテストの準備をする<br>例: `pre abc130`
  - まだ始まっていないコンテストなら始まるまで待つ
  - テストケースのダウンロードなどをする
  - 問題 a の入力を生成する
  - url の代わりにコンテスト id でもいい

- (ここでメインのソースコード(今は`example.cpp`)を編集)

- :heavy_check_mark: `submit [p]`: 整形して、問題 p のサンプルチェックをして、AC なら提出<br>例 `sub`
  - `-c`: ステータスにかかわらず、yn で提出するか選択(正答が複数ある問題など)
  - `-f`: コンパイルせずに提出

- :heavy_check_mark: `generate [p]`: 問題 p の入力を生成する<br>例: `g a`
  - メインのソースファイルにそのまま書き込まれる
  - 元あった内容は消去される

- 戻って次の問題を解く。

---

その他のコマンド

- :x: `case [n]`: テストケースを操作 追加、削除、クリップボードにコピーなど 未定
- :heavy_check_mark: `copy`: ソースコードを整形して、クリップボードにコピー(`submit` 未対応のコンテストサイトで)
- :heavy_check_mark: `clear`: solve 内、入力部分を消す 上手く生成されなかった時など
- :heavy_check_mark: `compile`: 整形してコンパイルする
- :heavy_check_mark: `run [n] [p]`: 実行する
  - n が指定なし: 標準入力から入力
  - n == 0: クリップボードから入力
  - n >= 1: (問題 p の) n 番目のテストケースを入力
- :heavy_minus_sign: `case`: テストケースを操作する
  - :heavy_check_mark: `copy [n]`: n 番目のテストケースをクリップボードにコピー
  - :x: `add [n]`: n 番目のテストケースを作成/変更
    - 標準入力から input output を入力する
    - 特別な文字を入力したら変更しない など
  - :x: `remove [n]`: n 番目のテストケースを削除
- :heavy_check_mark: `make-snippets`: [ライブラリ](https://tqk.blue/library/)からソースコードを持ってきてスニペット化する
  - (タイトル)[tab] と入力するとライブラリの中身が貼られる
    - (#include で提出されるときに埋め込まれるやつのほうがかっこいいが、ライブラリの中身をその場でいじりたいため悩んでいる)
    - 全部ラムダ式渡すようにしていじらないように変えるか、展開コマンドを用意するなど

## 対応するサイト

- :heavy_check_mark: AtCoder
- :x: ばちゃ AtCoder Problems
- :x: ~~ばちゃ AVC~~
- :x: CodeForces

## config
`ac/config.yml`
- `source_path`: メインのソースファイルの場所
- `template_path`: テンプレートファイルの場所 `generate` に使われる
- `snippets_path`: スニペットが生成される場所 `make-snippet` に
- `compile`: コンパイルコマンド
  - `{{source}}` で `source_path` を展開
- `execute`: 実行コマンド 上と合わせる
