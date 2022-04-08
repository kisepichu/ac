[![Test generate](https://github.com/tqkoh/ac/actions/workflows/test_generate.yaml/badge.svg)](https://github.com/tqkoh/ac/actions/workflows/test_generate.yaml)
[![Tqk](https://img.shields.io/endpoint?url=https%3A%2F%2Fatcoder-badges.now.sh%2Fapi%2Fatcoder%2Fjson%2FTqk)](https://atcoder.jp/users/Tqk)
[![Tqk](https://img.shields.io/endpoint?url=https%3A%2F%2Fatcoder-badges.now.sh%2Fapi%2Fcodeforces%2Fjson%2FTqk)](https://codeforces.com/profile/Tqk)

# **自分用**競プロツール備忘録(575)

- tqk の競プロツール
- 全ての人間用は [oj](https://github.com/online-judge-tools/oj) などが上位互換
- ツールというかコンテスト中の作業全部をするディレクトリ
- wsl1 Ubuntu 18.04 LTS

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

<details>
  <summary>やりたいこと</summary>
  
- 無駄な作業を消す
- コンテスト中に短いコマンドで、入力部分のソースコード( `int n; cin>>n;...` のこと)生成、サンプルテスト、提出などの操作をできるようにする
- コンテスト中にソースファイルを 1 個だけ使いまわす: デフォルトは `example.cpp` (実行すると生成される)
  - ファイル移動が面倒なため
- 各コマンドでは整形してから処理する:
  - 整形方法は [ac/command/sub/format.py](https://github.com/tqkoh/ac/blob/master/ac/command/sub/format.py) を編集すれば変えられる
  - 今の状態:
    - `//sub-BOF`から`//sub-EOF`までを抜き出す
    - 提出ページの一番上に summary を表示する
      - テンプレートが邪魔なため
      - solve 部分のみを切り取り最上部に表示
      - ライブラリを貼った部分は名前だけ表示
- 短く書く: <br>
~/.bashrc に追加するなど 例:
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
  
</details>

## コマンド

- コンテストに出るとき、この順に実行する
- p は指定しなければ前回実行時の問題番号が使われる(全コマンド共通)<br>なので基本 `generate` のみで p を指定する
- 実装済み: :heavy_check_mark:、未実装: :x:

---

- :heavy_check_mark: `init [url]`: コンテストの準備をする<br>例: `pre abc130`
  - コンテスト url の代わりにコンテスト id でもいい
  - まだ始まっていないコンテストなら始まるまで待ってから
  - テストケースのダウンロードなどをする
  - 問題 a の入力部分を生成する( `int n; cin>>n; ...` のこと)

- (ここで問題を解きメインのソースコード(今は`example.cpp`)を編集)

- :heavy_check_mark: `submit [p]`: 整形して、問題 p のサンプルチェックをして、AC なら提出する<br>例 `sub`
  - 提出したら消去して次の問題の入力部分を自動生成する
  - `-c`: ステータスにかかわらず、yn で提出するか選択(正答が複数ある問題など)
  - `-f`: コンパイル、サンプルチェックをせずに提出

- :heavy_check_mark: `generate [p]`: 問題 p の入力部分を生成する<br>例: `g b`
  - 問題のページから入力方法などを推測する。
  - Yes/No で答える場合などの答えの文字列、mod を取る問題の mod なども推測して埋め込む。詳しくは [template の書き方](https://github.com/tqkoh/ac#template-の書き方)
  - 解く順番を変える場合/提出したものが WA で後から戻る場合に使う
    - WA だったことがすぐわかったら、メインのソースを編集しているエディタで Ctrl+Z をして復元する

- 次の問題を解き `submit` に戻る。

---

その他のコマンド

- :heavy_check_mark: `copy`: ソースコードを整形して、クリップボードにコピー(`submit` 未対応のコンテストサイトで)
- :heavy_check_mark: `clear`: solve 内と入力部分を消す
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
- :heavy_check_mark: `make-snippets`: [ライブラリ](https://tqk.blue/library/)からソースコードを持ってきてスニペット化する(Visual Studio 2019 用)
  - (タイトル)[tab] と入力するとライブラリの中身が貼られる
    - #include で書いて、提出されるときに埋め込まれるやつもかっこいいが、ライブラリの中身をその場でいじりたいためこうしている

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

## template の書き方
[example_template.cpp](https://github.com/tqkoh/ac/blob/master/example_template.cpp) を見て
- `{% if [v] %}` のみ、(`{% else %}` のみ、)`{% endif %}` のみからなる行で、v が空でないかで場合分けできる
- `{{ [v] }}` で、v の中身を展開できる
  - 使える変数(全て文字列):
    - `prediction_success`: 入力部分の推測が失敗したなら空、そうでないなら空でない
    - `input_part`: 問題から推測した入力部分の C++ コード。
    - `formal_arguments`: solve の引数定義部分の C++ コード。`lint n, vector<lint> a` など
    - `mod`: 問題から推測した mod の値。`998244353` など
    - `yes_str`: 問題から推測した Yes に対応する答え。
    - `no_str`: 問題から推測した No に対応する答え。
    - `test_generate`: テスト用、`input_part` の後につける。
