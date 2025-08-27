<script>
  import Title from "$lib/Elements/Title.svelte"
  import Par from "$lib/Markup/Par.svelte"
  import Math from "$lib/Math/Math.svelte"
  import P from "$lib/Markup/P.svelte"
  import Heading from "$lib/Markup/Heading.svelte"
  import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
  import Codeblock from "$lib/Code/Codeblock.svelte"
  import Code from "$lib/Code/Code.svelte"
  import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Линейный конгруэнтный метод"
/>

<Par>
<P>
    Мы хотим генерировать случайное число с равномерным распределением на <Math m="[0, 1]"/>.
</P>
<P>
    Компьютер может хранить только числа конечного размера.
    Поэтому нам придется сгенерировать число, занимающее всё компьютерное слово.
    При таком подходе будем считать, что дробная точка стоит в начале этого слова.
</P>
</Par>

<Par>
<P>
    Посмотрим на наиболее часто применимый метод генерации таких простых чисел.
</P>
<P>
    Выберем волшебные числа:
    <Math m="m"/> &mdash; модуль, <Math m="a"/> &mdash; множитель и <Math m="c"/> &mdash; приращение.
    При этом <Math m="0 \le a \lt m"/> и <Math m="0 \le c \lt m"/>.
</P>
<P>
    Будем строить последовательность величин <Math m="x_n"/>, начиная с заранее выбранного числа <Math m="x_0"/>.
</P>
<Math display m={`x_{n+1} = (a \\cdot x_n + c) \\bmod m`}/>
</Par>

<Par>
<P>
    Последовательность имеет вид <Math m={`x_{n+1} = f(x_n)`}/>, где <Math m="f \colon \ZZ_m \to \ZZ_m"/>.
    Все такие последовательности имеют цикл, поэтому она когда-то начнет повторяться.
</P>
<P>
    Например, для <Math m="m = 10"/>, <Math m="a = 3"/> и <Math m="c = 5"/>
    при начальном значении <Math m="x_0 = 1"/> имеем последовательность
</P>
<Math display
      m="x_0 = 1 \quad x_1 = 8 \quad x_2 = 9 \quad x_3 = 2 \quad x_4 = 1 \quad x_5 = 8 \quad x_6 = 9 \quad x_7 = 2 \quad x_8 = 1"/>
</Par>

<Par>
<P>
    От значений констант <Math m="a"/> и <Math m="c"/> сильно зависит случайность последовательности и ее период.
</P>
<P>
    При <Math m="c=0"/> период последовательности может оказаться меньше, чем при <Math m={`c \\neq 0`}/>.
</P>
<P>
    При <Math m="a=0"/> последовательность вообще не случайна,
    а при <Math m="a=1"/> получаем <Math m={`x_{n+1} = (x_0 + nc) \\bmod m`}/>, что тоже так себе.
</P>
<P>
    Нам подходят только <Math m="a \ge 2"/> и <Math m="c \ge 1"/>.
</P>
</Par>

<Par>
<P>
    Можно обобщить формулу для последовательности, выразив <Math m="(n+k)"/>-й член через <Math m="n"/>-й.
</P>
<Math display m={`x_{n+k} = \\big( a^k \\cdot x_n + (a^k-1) / (a-1) \\cdot c \\big) \\bmod m`}/>
<P>
    Получаем, что подпоследовательность последовательности <Math m="x_n"/>, содержащая каждый <Math m="k"/>-й член,
    также является линейной конгруэнтной последовательностью
    с множителем <Math m="a^k"/> и приращением <Math m="(a^k-1) / (a-1) \cdot c"/>.
</P>
<P>
    Отсюда же можно получить общую формулу для <Math m="n"/>-го члена последовательности <Math m="x_n"/>:
</P>
<Math display m={`x_n = \\big( a^n \\cdot x_0 + (a^n-1) / (a-1) \\cdot c \\big) \\bmod m`}/>
</Par>


<Heading>Выбор модуля</Heading>

<Par>
<P>
    Какое значение выбрать для модуля <Math m="m"/>?
    Он должен быть достаточно большим, ведь период последовательности не может быть больше <Math m="m"/>.
    Еще нам бы хотелось, чтобы <Math m={`(a \\cdot x_n + c) \\bmod m`}/> вычислялось не слишком долго.
</P>
<P>
    Самый перспективный вариант выбора <Math m={`m`}/> &mdash; машинное слово.
    При таком выборе дорогую операцию <Math m={`\\bmod`}/> вообще делать не надо, ведь она выполняется автоматически.
</P>
<P>
    Код такого преобразования <Math m={`x \\mapsto (\\code{A} \\cdot x + \\code{C}) \\bmod w`}/>,
    где <Code c="A"/> и <Code c="C"/> &mdash; константы и <Math m={`w`}/> &mdash; машинное слово (я взял <Math m={`64`}/>-битное qword).
    В начале <Math m={`x`}/> будет хранится в регистре <Code language="asm" c="rax"/>,
    и результат вычислений окажется в том же регистре <Code language="asm" c="rax"/>.
    Все операции беззнаковые.
</P>
</Par>

<Codeblock language="asm" code={`
mov rax, x    ; x -> rax
imul A        ; rax * A -> rdx:rax
add rax, C    ; rax + C -> rax
`}/>

<Par>
<P>
    Иногда бывает нужно брать не <Math m={`m = w`}/>, а <Math m={`m = w + 1`}/>.
</P>
</Par>

<Codeblock language="asm" code={`
mov rax, x
`}/>


<Theorem title="Лемма о домножении">
<P>
    Пусть <Math m="p"/> &mdash; простое число, и <Math m="a"/> &mdash; такое число, что <Math m="p^a > 2"/>.
</P>
<P>
    Тогда если <Math m={`x \\eqmod{p^a} 1`}/> и <Math m={`x \\neqmod{p^{a+1}} 1`}/>
</P>
</Theorem>