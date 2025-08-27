<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
</script>

<Title title="Основы алгебры логики"
/>

<Par>
<P>
    Алгебра логики представляет собой алгебру над высказываниями.
    Нас интересует только истинность или ложность высказываний.
</P>
</Par>

<Heading>Бинарные операции</Heading>

<Par>
<P>
    Имеется <Math m={`16`}/> функций <Math m={`f \\colon \\{0, 1\\}^2 \\to \\{0, 1\\}`}/>,
    переводящих два бита <Math m={`x`}/> и <Math m={`y`}/> в один бит <Math m={`f(x, y)`}/>.
    Такие функции, следуя терминологии алгебры, называются <b>бинарными операциями</b> над битами.
</P>
</Par>

<table>
    <thead>
    <tr>
        <th>Таблица истинности</th>
        <th>Обозначения</th>
        <th>Символ оператора</th>
        <th>Название</th>
    </tr>
    </thead>

    <tbody>
    <tr>
        <td><Math m={`0000`}/></td>
        <td><Math m={`0`}/></td>
        <td><Math m={`\\mathbin{\\bot}`}/></td>
        <td>ложь</td>
    </tr>
    <tr>
        <td><Math m={`0001`}/></td>
        <td><Math m={`x \\land y`}/>, <Math m={`x \\cdot y`}/></td>
        <td><Math m={`\\land`}/></td>
        <td>конъюнкция, И</td>
    </tr>
    <tr>
        <td><Math m={`0010`}/></td>
        <td><Math m={`x \\land \\bar{y}`}/>, <Math m={`[x > y]`}/>, <Math m={`x \\dotminus y`}/></td>
        <td><Math m={`\\nRightarrow`}/></td>
        <td>отрицание импликации, НО НЕ</td>
    </tr>
    <tr>
        <td><Math m={`0011`}/></td>
        <td><Math m={`x`}/></td>
        <td><Math m={`\\mathbin{\\mathsf{L}}`}/></td>
        <td>левая проекция, первый</td>
    </tr>
    <tr>
        <td><Math m={`0100`}/></td>
        <td><Math m={`\\bar{x} \\land y`}/>, <Math m={`[y > x]`}/>, <Math m={`y \\dotminus x`}/></td>
        <td><Math m={`\\nLeftarrow`}/></td>
        <td>отрицание обратной импликации</td>
    </tr>
    <tr>
        <td><Math m={`0101`}/></td>
        <td><Math m={`y`}/></td>
        <td><Math m={`\\mathbin{\\mathsf{R}}`}/></td>
        <td>правая проекция, второй</td>
    </tr>
    <tr>
        <td><Math m={`0110`}/></td>
        <td><Math m={`x \\oplus y`}/>, <Math m={`x \\notequiv y`}/></td>
        <td><Math m={`\\oplus`}/></td>
        <td>исключающее ИЛИ, не эквиваленция</td>
    </tr>
    <tr>
        <td><Math m={`0111`}/></td>
        <td><Math m={`x \\lor y`}/></td>
        <td><Math m={`\\lor`}/></td>
        <td>дизъюнкция, ИЛИ</td>
    </tr>
    <tr>
        <td><Math m={`1000`}/></td>
        <td><Math m={`\\bar{x} \\land \\bar{y}`}/>, <Math m={`\\overline{x \\lor y}`}/>, <Math m={`x \\nlor y`}/></td>
        <td><Math m={`\\nlor`}/></td>
        <td>отрицание дизъюнкции, НЕ-ИЛИ</td>
    </tr>
    <tr>
        <td><Math m={`1001`}/></td>
        <td><Math m={`x \\equiv y`}/>, <Math m={`x \\Leftrightarrow y`}/></td>
        <td><Math m={`\\Leftrightarrow`}/></td>
        <td>эквиваленция</td>
    </tr>
    <tr>
        <td><Math m={`1010`}/></td>
        <td><Math m={`x  y`}/></td>
        <td><Math m={`\\mathbin{\\overline{\\mathsf{R}}}`}/></td>
        <td>правое дополнение, не второй</td>
    </tr>
    <tr>
        <td><Math m={`1011`}/></td>
        <td><Math m={`x  y`}/></td>
        <td><Math m={`\\Leftarrow`}/></td>
        <td>обратная импликация, ЕСЛИ</td>
    </tr>
    <tr>
        <td><Math m={`1100`}/></td>
        <td><Math m={`x  y`}/></td>
        <td><Math m={`\\mathbin{\\overline{\\mathsf{L}}}`}/></td>
        <td>левое дополнение, не первый</td>
    </tr>
    <tr>
        <td><Math m={`1101`}/></td>
        <td><Math m={`x  y`}/></td>
        <td><Math m={`\\Rightarrow`}/></td>
        <td>импликация, ЕСЛИ ... ТО</td>
    </tr>
    <tr>
        <td><Math m={`1110`}/></td>
        <td><Math m={`x  y`}/></td>
        <td><Math m={`\\nland`}/></td>
        <td>отрицание конъюнкции, НЕ И</td>
    </tr>
    <tr>
        <td><Math m={`1111`}/></td>
        <td><Math m={`1`}/></td>
        <td><Math m={`\\mathbin{\\top}`}/></td>
        <td>истина</td>
    </tr>

    </tbody>
</table>

<Par>
<P>
    Функция от двух переменных часто записывается в суффиксной нотации,
    то есть в виде оператора <Math m={`x * y`}/>, а не <Math m={`f(x, y)`}/>.
    Столбец &laquo;Символ оператора&raquo; как раз показывает символ,
    который нужно вставить вместо <Math m={`*`}/> для записи разных операций.
</P>
</Par>


<Subheading>И, ИЛИ и НЕ</Subheading>

<Par>
<P>
    Обе операции <Math m={`\\land`}/> и <Math m={`\\lor`}/> являются коммутативными и ассоциативными:
</P>
<Math display
      m={`x \\land y = y \\land x \\quad\\text{и}\\quad (x \\land y) \\land z = x \\land (y \\land z) \\\\!
          x \\lor y = y \\lor x \\quad\\text{и}\\quad (x \\lor y) \\lor z = x \\lor (y \\lor z) `}/>
<P>
    А ещё <Math m={`\\land`}/> дистрибутивна по <Math m={`\\lor`}/>,
    и наоборот, <Math m={`\\lor`}/> дистрибутивна по <Math m={`\\land`}/>:
</P>
<Math display
      m={`x \\land (y \\lor x) = (x \\land y) \\lor (x \\land z) \\quad\\text{и}\\quad
          x \\lor (y \\land z) = (x \\lor y) \\land (x \\lor z)`}/>
<P>
    Также работает идемпотентность
</P>
<Math display m={`x \\lor x = x \\quad\\text{и}\\quad x \\land x = x`}/>
<P>
    и поглощение
</P>
<Math display m={`x \\land (x \\lor y) = x \\quad\\text{и}\\quad x \\lor (x \\land y) = x`}/>

</Par>


<Subheading>Штрих Шеффера и стрелка Пирса</Subheading>

<Par>
<P>
    <b>Штрих Шеффера</b> &mdash; другое название операции НЕ-И.
    Эта операция введена Генри Шеффером в 1913 году.
    С помощью этой операции можно выразить все <Math m={`16`}/> бинарных операций.
</P>
</Par>

<Par>
<Math display
      m={`\\align{
          \\mathbin{\\bot} &\\colon \\bigl( x \\nland (x \\nland x) \\bigr) \\nland \\bigl( x \\nland (x \\nland x) \\bigr)  \\quad&\\quad
          \\nlor &\\colon \\bigl( x \\nland (x \\nland x) \\bigr) \\nland \\bigl( (x \\nland x) \\nland (y \\nland y) \\bigr) \\\\

          \\land &\\colon (x \\nland y) \\nland (x \\nland y) \\quad&\\quad
          \\Leftrightarrow &\\colon (x \\nland y) \\nland \\bigl( (x \\nland x) \\nland (y \\nland y) \\\\

          \\nRightarrow &\\colon \\bigl( x \\nland (x \\nland y) \\bigr) \\nland \\bigl( x \\nland (x \\nland y) \\bigr) \\quad&\\quad
          \\mathbin{\\overline{\\mathsf{R}}} &\\colon y \\nland y \\\\

          \\mathbin{\\mathsf{L}} &\\colon x \\quad&\\quad
          \\Leftarrow &\\colon y \\nland (x \\nland x) \\\\

          \\nLeftarrow &\\colon \\bigl( y \\nland (y \\nland x) \\bigr) \\nland \\bigl( y \\nland (y \\nland x)  \\quad&\\quad
          \\mathbin{\\overline{\\mathsf{L}}} &\\colon x \\nland x \\\\

          \\mathbin{\\mathsf{R}} &\\colon y \\quad&\\quad
          \\Rightarrow &\\colon x \\nland (x \\nland y) \\\\

          \\oplus &\\colon \\bigl( y \\nland (x \\nland x) \\bigr) \\nland \\bigl( x \\nland (x \\nland y) \\bigr) \\quad&\\quad
          \\nland &\\colon x \\nland y \\\\

          \\lor &\\colon (x \\nland x) \\nland (y \\nland y) \\quad&\\quad
          \\mathbin{\\top} &\\colon x \\nland (x \\nland x)
      }`}/>

</Par>


