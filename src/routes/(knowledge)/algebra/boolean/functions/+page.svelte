<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
</script>

<Title title="Булевы функции"
/>

<Par>
<P>
    <b>Булева функция</b> от <Math m={`n`}/> переменных &mdash; функция
    <Math m={`f \\colon \\{0, 1\\}^n \\to {0, 1}`}/>.
</P>
<P>
    Она принимает на вход <Math m={`n`}/> битов <Math m={`x_1, x_2, \\dotsc, x_n`}/>,
    и возвращает один бит <Math m={`f(x_1, x_2, \\dotsc, x_n)`}/>.
</P>
<P>
    Каждая булева функция от <Math m={`n`}/> переменных может быть определена своей таблицей истинности,
    состоящей из значений этой функции на всех <Math m={`2^n`}/> входах.
    Часто входы сортируют в лексикографическом порядке, и таблицу истинности пишут просто строкой
</P>
<Math display
      m={`f(0, 0, \\dotsc, 0, 0) \\quad f(0, 0, \\dotsc, 0, 1) \\quad f(0, 0, \\dotsc, 1, 0) \\quad f(0, 0, \\dotsc, 1, 1) \\quad \\cdots \\quad f(1, 1, \\dotsc, 1, 0) \\quad f(1, 1, \\dotsc, 1, 1)`}/>
</Par>

<Par>
<P>
    Все булевы функции можно выразить через бинарные операторы, изученные нами в разделе Основы алгебры логики.
</P>
</Par>


<Heading>Многочлены Жегалкина</Heading>

<Par>
<P>
    Жегалкин заметил, что любую булеву функцию можно представить в виде
</P>
<Math display
      m={`f(x_1, x_2, \\dotsc, x_{n-1}, x_n) = g(x_1, x_2, \\dotsc, x_{n-1}) \\oplus h(x_1, x_2, \\dotsc, x_{n-1}) \\land x_n`}/>
<P>
    где <Math m={`g(x_1, x_2, \\dotsc, x_{n-1}) = f(x_1, x_2, \\dotsc, x_{n-1}, 0)`}/>
    и <Math
        m={`h(x_1, x_2, \\dotsc, x_{n-1}) = f(x_1, x_2, \\dotsc, x_{n-1}, 0) \\oplus f(x_1, x_2, \\dotsc, x_{n-1}, 1)`}/>.
</P>

<P>
    Повторяя эту операцию итеративно для всех внутренних функций,
    можно получить разложение функции <Math m={`f`}/> в многочлен, называемый <b>многочленом Жегалкина</b>
</P>
<Math display
      m={`f(x_1, x_2, \\dotsc, x_{n-1}, x_n) =
          a_0 \\oplus \\bigoplus_{\\mathclap{\\substack{1 \\le k \\le n \\\\ 1 \\le j_1 < \\dotsb < j_k \\le n}}}
          a_{j_1, \\dotsc, j_k} \\land \\bigland_{s=1}^k x_{j_s}`}/>
<P>
    Операция <Math m={`\\oplus`}/> аналогична обычному сложению по модулю <Math m={`2`}/>,
    а операция <Math m={`\\land`}/> аналогична умножению, значит,
    многочлен Жегалкина можно переписать из булевой вида
    в вид многочлена из <Math m={`\\ZZ_2[x_1, x_2, \\dotsc, x_n]`}/>
</P>
<Math display
      m={`f(x_1, x_2, \\dotsc, x_{n-1}, x_n) =
          \\Biggl( a_0 + \\sum_{\\mathclap{\\substack{1 \\le k \\le n \\\\ 1 \\le j_1 < \\dotsb < j_k \\le n}}}
          a_{j_1, \\dotsc, j_k} \\cdot \\prod_{s=1}^k x_{j_s} \\Biggr) \\bmod 2`}/>
<P>
    Такой вид функции <Math m={`f(x_1, x_2, \\dotsc, x_n)`}/> ещё называется её мультилинейным представлением.
    Коэффициенты <Math m={`a_{j_1, \\dotsc, j_k} \\in \\{0, 1\\}`}/> показывают,
    содержится ли член <Math m={`\\prod_{s=1}^k x_{j_s}`}/> в представлении функции, или нет.
</P>
</Par>

<Subheading>Целочисленное мультилинейное представление</Subheading>




<Heading>Нормальные формы</Heading>

<Par>
<P>
    Джордж Буль разлагал функции по-другому
</P>
<Math display
      m={`f(x_1, x_2, \\dotsc, x_{n-1}, x_n) = \\bigr( g(x_1, x_2, \\dotsc, x_{n-1}) \\land x_n \\bigr)
          \\lor \\bigl( h(x_1, x_2, \\dotsc, x_{n-1}) \\land \\bar{x}_n \\big)`}/>
<P>
    где просто <Math m={`g(x_1, x_2, \\dotsc, x_{n-1}) = f(x_1, x_2, \\dotsc, x_{n-1}, 0)`}/>
    и <Math m={`h(x_1, x_2, \\dotsc, x_{n-1}) = f(x_1, x_2, \\dotsc, x_{n-1}, 1)`}/>.
</P>
<P>
    Аналогично, итеративно раскрывая внутренние функции, можно получить представление исходной функции
    в дизъюнктивной нормальной форме
</P>
<Math display
      m={`f(x_1, x_2, \\dotsc, x_{n-1}, x_n) =
          \\bigoplus_{\\mathclap{\\substack{1 \\le k \\le n \\\\ 1 \\le j_1 < \\dotsb < j_k \\le n}}}
          a_{j_1, \\dotsc, j_k} \\land \\bigland_{s=1}^k x_{j_s}`}/>

</Par>


<Subheading>Анализ импликант</Subheading>

<Par>
<P>
    Пусть <Math m={`f(x_1, x_2, \\dotsc, x_n)`}/> &mdash; одна из <Math m={`\\binom{2^n}{m}`}/> булевых функций,
    истинных только в <Math m={`m`}/> точках. И пусть такая функция выбирается случайно (равновероятно).
</P>
<P>
    С какой вероятностью <Math m={`\\bigland_{j=1}^k x_j = x_1 \\land x_2 \\land \\dotsb \\land x_k`}/>
    является импликантой функции <Math m={`f(x_1, x_2, \\dotsc, x_n)`}/>?
</P>
</Par>