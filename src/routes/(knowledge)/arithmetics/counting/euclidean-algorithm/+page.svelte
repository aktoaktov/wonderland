<script>
    import Heading from "$lib/Markup/Heading.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
</script>

<Title title="Алгоритм Евклида"
/>

<Definition title="Наибольший общий делитель">
    <P>
        <b>Наибольший общий делитель</b> чисел <Math m={`a`}/> и <Math m={`b`}/> &mdash; число
    </P>
    <Math display m={`\\gcd(a, b) \\defeq \\max\\{ g : g \\divides a \\land g \\divides b \\}`}/>
</Definition>

<Par>

    <P>
        Когда оба числа равны <Math m={`0`}/>, результат <Math m={`\\gcd(0, 0)`}/> не определен,
        так как подойдет любое число.
        Будем в таком случае считать, что <Math m={`\\gcd(0, 0) \\defeq 0`}/>.
        Тогда <Math m={`\\gcd(a, 0) = a`}/>.
    </P>
    <P>
        Тут надо сразу сказать важную вещь.
        Наибольший общий делитель существует не только для чисел, а для всего, что может делиться.
        Это определение, все дальнейшие утверждения и алгоритмы будут справедливы для любых
        коммутативных колец с единицей, в которых есть евклидова норма.
    </P>
    <P>
        Несколько примеров таких колец.
        Целые числа <Math m={`\\ZZ`}/> и евклидова норма <Math m={`a \\mapsto |a|`}/>,
        кольца многочленов <Math m={`\\RR[x]`}/> и евклидова норма <Math m={`P \\mapsto \\deg P`}/>,
        гауссовы числа <Math m={`\\ZZ[i]`}/> и евклидова норма <Math m={`(a + bi) \\mapsto a^2 + b^2`}/>.
    </P>
</Par>

<Par>
    <P>
        Для нахождения наибольшего общего делителя двух чисел можно применить <b>алгоритм Евклида</b>.
        Основан этот алгоритм на следующем факте
    </P>

    <Math display m={`\\gcd(a, b) = \\cases{a & \\if b = 0 \\\\ \\gcd(b, a - b) & \\otherwise}`}/>

    <P>
        Для ускорения вычислений можно сразу вычитать столько, сколько возможно.
        Получаем формулу, которую уже можно использовать
    </P>

    <Math display m={`\\gcd(a, b) = \\cases{a & \\if b = 0 \\\\ \\gcd(b, a \\bmod b) & \\otherwise}`}/>

    <P>
        Ну вот мы и получили алгоритм Евклида.
    </P>
</Par>

<Codeblock code={
`function gcd(int a, int b) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)`
}/>

<Par>
    <P>
        Можно избавиться от небольшого оверхеда в рекурсии, переписав через цикл
    </P>
</Par>

<Codeblock code={
`function gcd(int a, int b) -> int:
    while b > 0:
        a %= b
        swap a, b
    return a`
}/>

<Par>
    <P>
        Давайте грубо оценим время работы алгоритма.
        Каждую итерацию мы берем остаток от деления наибольшего числа на наименьшее,
        поэтому наибольшее число уменьшается минимум в два раза.
    </P>
    <P>
        Отсюда получается, что алгоритм работает за время <Math m={`O\\left( \\log \\big( \\min(a, b) \\big) \\right)`}/>.
    </P>
</Par>


<Heading>Расширенный алгоритм Евклида</Heading>


<Heading>Быстрый алгоритм Евклида</Heading>

<Par>
    <P>
        Для быстрого вычисления наибольшего общего делителя двух чисел можно применить следующий факт
    </P>
    <Math display m={`\\gcd(a \\cdot b, a \\cdot c) = a \\cdot \\gcd(b, c)`}/>
</Par>