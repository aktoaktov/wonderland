<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Image from "$lib/Elements/Image.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
</script>

<Title title="Скошенные деревья"
/>

<Par>
<P>
    При анализе алгоритмов на деревьях очень часто нужно знать длины путей от корня к узлам,
    глубину и прочие комбинаторные показатели.
    Полезно ввести дополнительные объекты, чтобы потом было проще.
</P>
</Par>

<Heading>Балансировка на высоте</Heading>

<Par>
<P>
    Часто бывает полезно заменить пустые поддеревья на фиктивные узлы.
    Такие узлы называются <b>фиктивные листы</b>, и представляют собой фиктивные вершины, подвешенные к листам дерева.
    В некоторой англоязычной литературе обычные узлы дерева называют <b>внутренними</b> листами,
    а фиктивные листы &mdash; <b>внешними</b> узлами.
    Так страдает интуиция, поэтому я такое обозначение использовать не буду.
</P>
</Par>

<Image src={""}>Фиктивные листы дерева</Image>

<Par>
<P>
    Важная характеристика дерева &mdash; длина кратчайшего пути
    от заданного узла <Math m={`v`}/> до какого-то фиктивного листа.
</P>
<Math display
      m={`s(v) \\defeq \\cases{
          0 & \\if v ~\\text{фиктивный лист} \\\\
          \\min \\bigl( s(v.\\code{left}), s(v.\\code{right}) \\bigr) + 1 & \\otherwise
          }`}/>
</Par>


<Heading>Балансировка на весе</Heading>
