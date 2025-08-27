<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
</script>

<Title title="Сериализация"
/>

<Par>
    <P>
        Очень часто бывает нужно существующий внутри программы объект
        сохранить в файл, передать по сети или отдать другому процессу. Для
        этого нужно превратить этот объект в набор байт, который затем мы
        сможем прочитать и восстановить исходный объект.
    </P>
</Par>

<Definition title="Сериализация">
    <b>Сериализация</b> &mdash; процесс превращения состояния объекта в битовую
    последовательность. Обратный процесс восстановления данных из битовой
    последовательности называется <b>десериализацией</b>.
</Definition>

<Definition title="Маршалинг">
    <b>Маршалинг</b> (marshalling, упорядочивать) &mdash; процесс преобразования
    данных из оперативной памяти в формат, пригодный для хранения или
    передачи.
</Definition>

<Par>
    <P>
        Сериализация и десериализация делаются по правилам, называемыми
        форматом сериализации. Все форматы можно разделить на человекочитаемые
        (JSON, XML, CSV) и человеко<b>не</b>читаемые (pickle, CBOR).
    </P>
    <P>
        Для начала определяется формат сериализации простых типов (чисел,
        строк, <Code c="true"/>/<Code c="false"/>), а затем способ их комбинации в более сложные
        объекты. Обычно более сложные объекты &mdash; это массивы (упорядоченный
        набор элементов) и ассоциативные массивы, ключи которых &mdash; простые
        типы, а значения любые.
    </P>
    <P>
        Некоторые форматы сериализации определяют дополнительные типы: дата,
        время, <Code c="none"/> и так далее.
    </P>
</Par>


<Heading>Простые типы</Heading>

<Par>
    <P>
        Здесь мы разберем общие подходы к сериализации простых типов
    </P>
</Par>

<Subheading>Числа</Subheading>

<Par>
    <P>
        Числа, в какой бы системе счисления они не были, остаются числами.
        Для нашей цели передать информацию достаточно представить числа в какой-то одной системе счисления.
    </P>
    <P>
        Самый простой вариант &mdash; просто записать число по символам.
    </P>
</Par>


<Heading>Человекочитаемые форматы</Heading>

<Subheading>JSON</Subheading>

<Par>
    <P>
        JSON (JavaScript Object Notation) &mdash; ...
    </P>
</Par>

<Codeblock language="bnf" code={
`<json> ::= <primitive> | <container>

<primitive> ::= <number> | <string> | <boolean>
<number> is a valid real number expressed in one of a number of given formats
<string> is a string of valid characters enclosed in quotes
<boolean> ::= true | false | null

<container> ::= <object> | <array>
<array> ::= '[' [ <json> *(', ' <json>) ] ']'
<object> ::= '{' [ <member> *(', ' <member>) ] '}'
<member> ::= <string> ': ' <json>`
}/>