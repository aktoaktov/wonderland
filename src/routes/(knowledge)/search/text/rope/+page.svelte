<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Statement from "$lib/Stencils/Blocks/Statement.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Math from "$lib/Math/Math.svelte"
</script>

<Title title="Строп"
/>

<Par>
    <P>
        Представим текстовый редактор.
        Задача текстового редактора &mdash; хранить текст в памяти, отображать его,
        и, самое главное, позволять редактировать текст.
    </P>
    <P>
        Можно, конечно, использовать наивный подход к хранению текста в памяти просто в виде последовательности байт.
        При добавлении одного символа куда-то в начало нам придется сдвигать в памяти почти весь текст.
        А ведь сам текст может быть огромным, например какая-нибудь книга типа &laquo;Война и мир&raquo;.
    </P>
    <P>
        Еще у нас есть операции удаления символов (наборов символов), замены символов и, иногда, поиска.
        В общем заключаем, что для эффективной работы с большими текстами наивного подхода недостаточно.
    </P>
</Par>

<Statement title="Строп">
    <P>
        <b>Строп</b> (rope) &mdash; структура данных для работы с большими строками, обеспечивающая эффективные
        операции конкатенации, вставки, удаления и индексации.
    </P>
    <P>
        Основная идея &mdash; представление строки в виде бинарного дерева,
        где листья содержат фрагменты строки, а внутренние узлы хранят метаданные для связи и балансировки.
    </P>
</Statement>

<Subheading>Структура узлов</Subheading>

<Par>
    <P>
        Как я уже упомянул в основной идее, нам нужно два типа узлов: терминальный и внутренний.
    </P>
    <P>
        В терминальном узле будем хранить саму подстроку <Code c="string value"/>.
        Во внутреннем узле мы храним дочерние узлы <Code c="left"/> и <Code c="right"/>.
        Для каждого узла будем ещё хранить полную длину левого поддерева, называемую весом.
        Эта информация нужна для реализации индексации.
    </P>
    <P>
        Ну и для оптимизации можно в каждом узле в поле <Code c="int length"/> хранить
        полную длину дерева с корнем в этом узле.
    </P>
    <P>
        Можно реализовывать две структуры: одна для терминального узла, другая для внутреннего.
        А можно реализовать одну общую структуру.
        Критерием терминальности узла будет просто отсутствующее значение у <Code c="value"/>.
    </P>
</Par>

<Codeblock code={
`struct node:
    node left
    node right

    string value
    int weight
    int length`
}/>

<Par>
    <P>
        У нас получается инвариант <Math m={`\\code{v.weight} = \\code{v.left.length}`}/>
        и <Math m={`\\code{v.length} = \\code{v.left.length} + \\code{v.right.length}`}/>.
        При этом для терминальной вершины <Code c="t"/> имеем <Math m={`\\code{t.weight} = 0`}/>,
        что логично, ведь у терминальной вершины нет поддеревьев.
    </P>
</Par>


<Subheading>Индексация</Subheading>

<Par>
    <P>
        Базовая операция, индексация, &mdash; получение символа по его индексу.
    </P>
</Par>

<Codeblock code={
`function get_char(node rope, int i) -> char:
    if rope.value is not none:  # если это терминальный узел
        return rope.value[i]

    if i < rope.weight:
        return get_char(rope.left, i)
    else:
        return get_char(rope.right, i - rope.weight)`
}/>


<Subheading>Вставка и удаление</Subheading>


<Subheading>Конкатенация и разделение</Subheading>

<Par>
    <P>
        Для конкатенации двух стропов достаточно просто создать новый узел и прицепить к нему оба стропа.
    </P>
</Par>

<Codeblock code={
`function concat(node s1, node s2) -> node:
    rope = new node()
    rope.left = s1
    rope.right = s2
    rope.weight = s1.length
    rope.length = s1.length + s2.length

    return rope`
}/>

<Par>
    <P>
        Временная сложность такой операции, очевидно, <Math m={`O(1)`}/>.
    </P>
</Par>

<Subheading>Получение среза</Subheading>