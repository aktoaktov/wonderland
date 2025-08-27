<script>
    import Title from "$lib/Elements/Title.svelte"
    import P from "$lib/Markup/P.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Math from "$lib/Math/Math.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Image from "$lib/Elements/Image.svelte"

    import imageLinkedListInMemory from "./linked-list-in-memory.svg"
</script>

<Title title="Линейные и связные списки"
/>

<Par>
<P>
    Давайте обсудим способы линейного представления набора данных.
    Хранить данные из набора мы будем в линейном списке.
</P>
<P>
    <b>Линейный список</b> &mdash; последовательность узлов (nodes), в которых хранятся записи.
    Все <Math m="n"/> узлов <Math m="x_1, x_2, \dotsc, x_n"/> таковы,
    что узел <Math m="x_k"/> следует за узлом <Math m={`x_{k-1}`}/> и предшествует узлу <Math m={`x_{k+1}`}/>
    для всех <Math m="1 < k < n"/>.
</P>
<P>
    Обращаю внимание на то, что это только логическая упорядоченность.
    Физически узлы могут располагаться как угодно, какие-то узлы даже могут физически отсутствовать,
    главное чтобы логическая связь была такой.
</P>
<P>
    С элементами линейного списка обычно совершаются следующие операции
</P>

<EnumList>
    <ListItem>
        Получение доступа к <Math m="k"/>-му узлу списка для чтения, изменения полей записи и т.д.
    </ListItem>
    <ListItem>
        Вставка нового узла сразу после или до <Math m="k"/>-го узла списка
    </ListItem>
    <ListItem>
        Удаление <Math m="k"/>-го узла из списка
    </ListItem>
    <ListItem>
        Объединение нескольких списков в один
    </ListItem>
    <ListItem>
        Разбиение одного списка на несколько
    </ListItem>
    <ListItem>
        Создание копии списка
    </ListItem>
</EnumList>
</Par>

<Par>
<P>
    Сделать структуру данных, которая бы эффективно выполняла все эти операции очень сложно.
    На самом деле для большинства задач это и не нужно.
</P>
<P>
    Отдельного внимания заслуживают операции 1-3 при граничных случаях <Math m="k=1"/> и <Math m="k=n"/>.
    При таком условии эти операции можно выполнять в общем случае эффективнее и проще.
</P>
</Par>


<Heading>Односвязные списки</Heading>

<Par>
<P>
    Линейные списки линейными делает логическая упорядоченность.
    Естественно желание превратить логическую упорядоченность в физическую.
</P>
<P>
    Назовем каждый элемент линейного списка узлом, и будем в узле, помимо данных,
    хранить ещё и ссылку на следующий узел.
    Таким образом мы сможем физически упорядочить данные в памяти.
    Структура узла выглядит так
</P>
</Par>

<Codeblock code={
`struct node:
    node next
    some additional data`
}/>

<Par>
<P>
    Такой линейный список называется <b>связным</b> (односвязным), ведь у каждого узла есть связь со следующим.
</P>
</Par>

<Par>
<P>
    В памяти связные списки могут располагаться как угодно.
    Это значит, что время, затрачиваемое на все операции с узлами, не зависит от размера списка.
</P>
</Par>

<Image src={imageLinkedListInMemory}>Связный список в памяти</Image>


<Heading>Двусвязные списки</Heading>

<Par>
<P>
    В каждый узел связного списка можно включить не одну. а две связи: на следующий и на предыдущий узлы.
</P>
</Par>

<Codeblock code={
`struct node:
    node previous
    node next
    ...data...`
}/>


<Heading>Полуторасвязный список</Heading>

<Par>
<P>
    Sparse list
</P>
</Par>


<Heading>XOR список</Heading>

<Par>
<P>

</P>
</Par>


<Heading>Развёрнутый список</Heading>