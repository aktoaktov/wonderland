<script>
    import Math from "$lib/Math/Math.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
</script>

<Title title="Множества и операции над множествами"
/>


<Par>
    <P>
        <b>Множество</b> &mdash; это набор каких-то объектов, базовое неопределяемое понятие в математике.
        Множества состоят из элементов.
        Если <Math m="x"/> является элементом множества <Math m="S"/>,
        то пишут <Math m="x \in S"/> или <Math m="S \ni x"/>.
        Обратное этому утверждение, если элемент <Math m="x"/> не является элементом множества <Math m="S"/>,
        обозначают <Math m="x \notin S"/> или <Math m="S \notni x"/>.
    </P>
    <Math display m={`\\begin{align*}
    x \\in S = S \\ni x &\\defequiv \\text{элемент}~ x ~\\text{содержится в множестве}~ S \\\\
    x \\notin S = S \\notni x &\\defequiv \\text{элемент}~ x ~\\text{не содержится в множестве}~ S
    \\end{align*}`}/>
    <P>
        Один из способов задать множество &mdash; просто перечислить все его элементы. Например,
        множество
    </P>
    <Math display m={`X = \\big\\{ 1, 2, \\{7, 3\\}, \\text{кастрюля} \\big\\}`}/>
    <P>
        Множество, не содержащее ни одного элемента, называется <b>пустым</b> и записывается
        как <Math m="\nothing"/>.
    </P>
</Par>

<Definition title="Подмножество">
    <P>
        Множество <Math m="A"/> является <b>подмножеством</b> множества <Math m="B"/>,
        если каждый элемент множества <Math m="A"/> является элементом множества <Math m="B"/>.
        Этот факт записывается как <Math m="A \subset B"/>.
    </P>
    <Math display m={`A \\subset B \\defequiv \\forall x \\in A \\? x \\in B`}/>
</Definition>

<Par>
    <P>
        Например, <Math m={`\\{ 1, 3, 6 \\} \\subset \\{1, 2, 3, 4, 5, 6, 7\\}`}/>.
        Также <Math m={`\\{\\text{четные числа}\\} \\subset \\NN`}/>.
    </P>
    <P>
        Пустое множество является подмножеством любого множества.
        Иногда об это можно сильно споткнуться.
    </P>
</Par>

<Par>
    <P>
        Подмножество <Math m="A"/> множества <Math m="B"/> можно задать, выделив свойство, которым обладают все
        его элементы
    </P>
    <Math display m={`A = \\{x \\in B \\colon x ~\\text{обладает свойством}\\}`}/>
</Par>

<Par>
    <P>
        Совпадение всех элементов множеств <Math m="A"/> и <Math m="B"/> называется равенством и
        записывается <Math m="A = B"/>.
    </P>
    <Math display m="A \subset B \land B \subset A \iff A = B"/>

    <P>
        Пишут <Math m="A \subsetneq B"/>, если <Math m="A \subset B"/> и одновременно <Math m="A \neq B"/>, то
        есть <Math m="A"/> строго внутри <Math m="B"/>.
        Если надо подчеркнуть, что множества могут быть равны, то пишут
        <Math m="A \subseteq B"/>. Там, где это необходимо, я буду это явно указывать.
    </P>

    <P>
        Я буду везде, где это не принципиально, писать <Math m="A \subset B"/>.
    </P>
</Par>


<Heading>Операции над множествами</Heading>


<Definition title="Объединение и пересечение">
    <P>
        <b>Объединением</b> множеств <Math m="A"/> и <Math m="B"/> называется множество
        <Math m={`A \\union B \\defeq \\{ x \\colon x \\in A \\lor x \\in B \\}`}/>
    </P>
    <P>
        <b>Пересечением</b> множеств <Math m="A"/> и <Math m="B"/> называется множество
        <Math m={`A \\sect B \\defeq \\{ x \\colon x \\in A \\land x \\in B \\}`}/>
    </P>
</Definition>

<Par>
    <P>Обе эти операции являются ассоциативными и коммутативными, то есть</P>
    <Math display m={`A \\union B = B \\union A \\quad \\text{и} \\quad (A \\union B) \\union C = A \\union (B \\union C) \\\\[0.5em]
                        A \\sect B = B \\sect A \\quad \\text{и} \\quad (A \\sect B) \\sect C = A \\sect (B \\sect C)`}/>
    <P>Пересечение дистрибутивно по объединению и наоборот</P>
    <Math display m={`A \\union (B \\sect C) = (A \\union B) \\sect (A \\union C) \\quad \\text{и} \\quad
                        A \\sect (B \\union C) = (A \\sect B) \\union (A \\sect C)`}/>
    <P>
        Пересечение приоритетнее объединения, как умножение приоритетнее сложения. Но в длинных формулах лучше
        все-таки ставить скобки, глаз может неправильно воспринять порядок очень похожих друг на друга
        символов.
    </P>
</Par>

<Par>
    <P>
        Количество элементов в объединении множеств можно вычислить, зная количество элементов в каждом из
        этих множеств и количество элементов во всех возможных пересечениях этих множеств
    </P>
</Par>

<Theorem title="Формула включений-исключений">
    <P>
        Пусть <Math m="A_1, A_2, \\dotsc, A_n \\subset X"/>. Мощность объединения всех этих множеств можно
        вычислить по
        страшной формуле
    </P>

    <Math display
          m={`\\left|\\, \\bigunion_{i = 1}^n A_i \\,\\right| =
          \\sum_{\\nothing \\neq I \\subseteq \\{1, ..., n\\}} (-1)^{|I|+1} \\cdot \\left|\\, \\bigsect_{i \\in I} A_i \\,\\right|`}/>

    <P>Более гуманный, но не менее страшный вариант</P>

    <Math display
          m={`\\left|\\, \\bigunion_{i = 1}^n A_i \\,\\right| =
          \\sum_{k=1}^n \\, (-1)^{k+1} \\cdot \\sum_{1 \\le i_1 \\lt i_2 \\lt \\cdots \\lt i_k \\le n}
          |A_{i_1} \\sect A_{i_2} \\sect \\cdots \\sect A_{i_k}|`}/>

</Theorem>

<Par>
    <P>Для двух множеств формула принимает очень даже милый вид <Math m="|A \union B| = |A| + |B| - |A \sect B|"/></P>
    <P>
        Да и для трех множеств тоже ничего
    </P>
    <Math display
          m="|A \union B \union C| = |A| + |B| + |C| - |A \sect B| - |B \sect C| - |C \sect A| + |A \sect B \sect C|"/>
</Par>

<Par>
    <P>Доказать эту формулу можно посчитав количество вхождений элемента <Math
            m={`x \\in \\bigsect_{j = 1}^m A_{i_j}`}/> в правую часть формулы.</P>
    <Math display
          m={`k = (-1)^{m+1} \\cdot \\binom{m}{m} + (-1)^m \\cdot \\binom{m}{m-1} + \\cdots + (-1)^2 \\cdot \\binom{m}{1} = \\binom{m}{0} - \\sum_{i=0}^m\\, (-1)^i \\cdot \\binom{m}{i} = 1`}/>
</Par>

