<script lang="ts">
    import Category from "./Category.svelte"
    import Item from "./Item.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Chapter from "./Chapter.svelte"
</script>

<svelte:head>
    <title>Сценарий</title>
</svelte:head>

<Heading>Математика и анализ</Heading>
<Chapter>
    <Category title="Основы">
        <Item link="/math/basics/sets">Множества</Item>
        <Item link="/math/basics/functions">Функции и отображения</Item>
        <Item link="/math/basics/measure">Мера</Item>
        <Item link="/math/basics/metric-spaces">Метрические пространства</Item>
        <Item link="/math/basics/relations">Отношения</Item>
    </Category>
    <Category title="Специальные числа">
        <Item link="/math/special/harmonic-numbers">Гармонические числа</Item>
        <Item link="/math/special/bernoulli-numbers">Числа Бернулли</Item>
        <Item link="/math/special/stirling-numbers">Числа Стирлинга</Item>
    </Category>
    <Category title="Рекурренты">
        <Item link="/math/recurrences/linear">Линейные рекурренты</Item>
    </Category>
    <Category title="Последовательности">
        <Item link="/math/sequences/basics">Последовательности</Item>
        <Item link="/math/sequences/series">Ряды</Item>
        <Item link="/math/sequences/generating-functions">Производящие функции</Item>
    </Category>
    <Category title="Языки и смыслы">
        <Item link="/math/languages/formal-languages">Формальные языки</Item>
        <Item link="/math/languages/information">Информация и интерпретация</Item>
        <Item planned>Формальные грамматики</Item>
    </Category>
</Chapter>

<Heading>Исчисление</Heading>
<Chapter>
    <Category title="Свойства функций">
        <Item planned>Непрерывность</Item>
        <Item link="/calculus/function-properties/lipschitzs">Липшицевость</Item>
    </Category>

    <Category title="Дифференциальное исчисление">
        <Item link="/calculus/differential-calculus/derivative-and-gradient">Производные и градиенты</Item>
        <Item link="/calculus/differential-calculus/taylor-series">Ряды Тейлора</Item>
        <Item link="/calculus/differential-calculus/discrete">Дискретное дифференцирование</Item>
        <Item planned>Разделенные разности</Item>
    </Category>
</Chapter>

<Heading>Информационные структуры</Heading>
<Chapter>
    <Category title="Скалярные типы и записи">
        <Item link="/structures/scalar/simple-types">Простые типы</Item>
        <Item link="/structures/scalar/structures">Структуры</Item>
    </Category>

    <Category title="Линейные структуры">
        <Item link="/structures/linear/linked-lists">Линейные и связные списки</Item>
        <Item link="/structures/linear/stacks-queues-deques">Стеки, очереди, деки</Item>
        <Item planned>Последовательности</Item>
        <Item planned>Циклические списки</Item>
        <Item planned>Статические массивы</Item>
        <Item link="/structures/linear/iterators">Итераторы</Item>
        <Item planned>Ортогональные списки</Item>
    </Category>

    <Category title="Деревья">
        <Item link="/structures/trees/basics">Деревья</Item>
        <Item link="/structures/trees/skew-trees">Скошенные деревья</Item>
    </Category>

    <Category title="Многосвязные структуры">
        <Item planned>...</Item>
    </Category>

    <Category title="Динамические структуры">
        <Item planned>Link-Cut trees</Item>
        <Item planned>Euler Tour trees</Item>
        <Item planned>Top trees</Item>
        <Item planned>Holm–de Lichtenberg–Thorup</Item>
        <Item planned>Дерево Фенвика</Item>
        <Item planned>Дерево отрезков</Item>
    </Category>

    <Category title="Компактные структуры">
        <Item link="/structures/succinct/RSD">RSD и компактификация</Item>
        <Item planned>Компактные деревья</Item>
        <Item planned>Разреженные массивы</Item>
    </Category>
</Chapter>


<Heading>Арифметика и численные методы</Heading>
<Chapter>
    <Category title="Счёт">
        <Item link="/arithmetics/counting/positional-notation">Позиционные системы счисления</Item>
        <Item link="/arithmetics/counting/euclidean-algorithm">Алгоритм Евклида</Item>
        <Item planned>Арифметика интервалов</Item>
    </Category>

    <Category title="Арифметика с плавающей точкой">
        <Item planned>Числа с плавающей точкой</Item>
        <Item planned>Вычисления с одинарной точностью</Item>
        <Item optional>Вычисления с двойной точностью</Item>
        <Item planned>Погрешность вычислений</Item>
        <Item planned>Алгоритмы точного суммирования</Item>
        <Item planned>Умножение и деление с контролем ошибок</Item>
    </Category>

    <Category title="Специальные вычисления">
        <Item>Функции Бесселя</Item>
    </Category>

    <Category title="Интерполяция">
        <Item link="/arithmetics/interpolation/polynomials">Интерполяционные многочлены</Item>
        <Item planned>Сплайны</Item>
        <Item planned>Кривые Безье</Item>
        <Item link="/arithmetics/interpolation/uniform-interpolation">Равномерное приближение</Item>
    </Category>

    <Category title="Аппроксимация">
        <Item planned>Цепные дроби</Item>
        <Item planned>Аппроксимация Паде</Item>
    </Category>

    <Category title="Модулярная арифметика">
        <Item link="/arithmetics/modular/basics">Основы модулярной арифметики</Item>
        <Item link="/arithmetics/modular/crt">Китайская теорема об остатках</Item>
        <Item link="/arithmetics/modular/montgomery-space">Пространство Монтгомери</Item>
    </Category>

    <Category title="Простота и делимость">
        <Item link="/arithmetics/primes-and-divisibility/basics">Делимость</Item>
        <Item link="/arithmetics/primes-and-divisibility/sieve">Решета</Item>
        <Item link="/arithmetics/primes-and-divisibility/tests">Тесты на простоту</Item>
    </Category>
</Chapter>


<Heading>Алгебра</Heading>
<Chapter>
    <Category title="Структуры и операции">
        <Item link="/algebra/structures-and-operations/algebras">Алгебраические структуры</Item>
        <Item link="/algebra/structures-and-operations/fast-pow">Быстрое возведение в степень</Item>
    </Category>

    <Category title="Перестановки">
        <Item link="/algebra/permutations/permutations">Перестановки</Item>
        <Item link="/algebra/permutations/matrices">Матрицы перестановок</Item>
    </Category>

    <Category title="Теория групп">
        <Item link="/algebra/groups/basics">Группы</Item>
        <Item link="/algebra/groups/homomorphisms">Гомоморфизмы групп</Item>
        <Item link="/algebra/groups/actions">Действия групп</Item>
    </Category>

    <Category title="Многочлены">
        <Item link="/algebra/polynomials/basics">Многочлены и ряды</Item>
        <Item link="/algebra/polynomials/fdft">Дискретное преобразование Фурье</Item>
        <Item planned>Длинная арифметика</Item>
        <Item link="/algebra/polynomials/fast-multiplication">Быстрое умножение</Item>
    </Category>

    <Category title="Булева алгебра">
        <Item link="/algebra/boolean/basics">Основы алгебры логики</Item>
        <Item link="/algebra/boolean/functions">Булевы функции</Item>
        <Item link="/algebra/boolean/medians">Медианы</Item>
        <Item link="/algebra/boolean/threshold-functions">Пороговые функции</Item>
    </Category>

    <Category title="Векторы и матрицы">
        <Item planned>Векторные пространства</Item>
        <Item planned>Собственные значения и вектора</Item>
    </Category>

    <Category title="Решение СЛАУ">
        <Item link="/algebra/linear-systems/gauss">Метод Гаусса</Item>
        <Item planned>LU и LL разложения</Item>
        <Item planned>Метод Крамера</Item>
        <Item planned>Итерационные методы (Якоби, Гаусса-Зейделя, SOR)</Item>
    </Category>

    <Category title="Разреженные матрицы">
        <Item planned>Разреженные матрицы</Item>
    </Category>
</Chapter>


<Heading>Теория вероятностей и статистика</Heading>
<Chapter>
    <Category title="Вероятность">
        <Item link="/probability-theory/probability/discrete">Дискретная вероятность</Item>
        <Item link="/probability-theory/probability/entropy">Энтропия</Item>
    </Category>

    <Category title="Случайные величины">
        <Item planned>Случайные величины</Item>
    </Category>

    <Category title="Численные характеристики">
        <Item link="/probability-theory/numerical-characteristics/expected-value">Математическое ожидание</Item>
        <Item link="/probability-theory/numerical-characteristics/chebyshevs-inequality">Неравенства Чебышёва</Item>
        <Item link="/probability-theory/numerical-characteristics/chernoffs-bounds">Оценки Чернова</Item>
    </Category>

    <Category title="Предельные теоремы">
        <Item link="/probability-theory/limits/convergence">Сходимость</Item>
        <Item link="/probability-theory/limits/law-of-large-numbers">Законы больших чисел</Item>
        <Item link="/probability-theory/limits/central-limit-theorem">Центральная предельная теорема</Item>
    </Category>

    <Category title="Статистики и оценки">
        <Item planned>Выборки и статистики</Item>
        <Item link="/probability-theory/stats/estimations">Оценки</Item>
    </Category>

    <Category title="Проверка гипотез">
        <Item link="/probability-theory/statistical-hypothesis/hypothesis">Гипотезы и статистические критерии</Item>
        <Item planned>t-тесты</Item>
        <Item planned>F-тест и тест на нормальность</Item>
        <Item planned>Ранговые тесты</Item>
        <Item planned>Критерий Колмогорова-Смирнова</Item>
        <Item link="/probability-theory/statistical-hypothesis/pearson">Критерий Пирсона</Item>
    </Category>
</Chapter>


<Heading>Сортировка</Heading>
<Chapter>
    <Category title="Внутренняя сортировка">
        <Item link="/sorting/internal-sorting/insertion">Сортировка вставками</Item>
        <Item link="/sorting/internal-sorting/exchanging">Сортировка обменами</Item>
        <Item planned>Сортировка выбором</Item>
        <Item planned>Сортировка слиянием</Item>
        <Item link="/sorting/internal-sorting/optimum">Оптимальная сортировка</Item>
    </Category>

    <Category title="Приоритетные очереди">
        <Item link="/sorting/priority-queues/binary-heap">Бинарная и d-арная кучи</Item>
        <Item planned>Толстая куча</Item>
        <Item planned>Тонкая куча</Item>
        <Item planned>2-3 куча</Item>
    </Category>

    <Category title="Сливаемые кучи">
        <Item link="/sorting/mergeable-heaps/skew-heaps">Скошенная и левосторонняя кучи</Item>
        <Item planned>Биномиальная куча</Item>
        <Item planned>Фибоначчиева куча</Item>
        <Item planned>Спаренная куча</Item>
        <Item planned>Куча Бродала-Окасаки</Item>
    </Category>

    <Category title="Двусторонние приоритетные очереди">
        <Item planned>Двуродительская куча</Item>
        <Item planned>Дековая куча</Item>
        <Item planned> куча</Item>
    </Category>

    <Category title="Сортировка за линейное время">
        <Item planned>Сортировка подсчетом</Item>
        <Item planned>Поразрядная сортировка</Item>
    </Category>

    <Category title="Поиск статистик">
        <Item planned>Подсчёт порядковых статистик</Item>
    </Category>

    <Category title="Сортирующие сети">
        <Item planned>Сети компараторов</Item>
    </Category>
</Chapter>


<Heading>Поиск</Heading>
<Chapter>
    <Category title="Поиск">
        <Item link="/search/simple-search/search-structures">Поисковые структуры</Item>
        <Item link="/search/simple-search/sequential-search">Последовательный поиск</Item>
        <Item link="/search/simple-search/comparison-search">Поиск сравнениями</Item>
        <Item link="/search/simple-search/interpolation-search">Интерполяционный поиск</Item>
        <Item planned>Бинарное дерево поиска</Item>
        <Item planned>Битсет</Item>
    </Category>

    <Category title="Самобалансирующиеся деревья">
        <Item link="/search/self-balancing-trees/avl-tree">AVL дерево</Item>
        <Item planned>Красно-черное дерево</Item>
        <Item planned>Splay дерево</Item>
        <Item planned>Весовое дерево</Item>
        <Item planned>Scapegoat дерево</Item>
    </Category>

    <Category title="Кусты">
        <Item link="/search/bushy-trees/b-tree">B-дерево</Item>
        <Item planned>Танцующее дерево</Item>
        <Item planned>T-дерево</Item>
        <Item planned>Экспоненциальное дерево Андерсона</Item>
    </Category>

    <Category title="Боры">
        <Item link="/search/tries/trie">Бор</Item>
        <Item link="/search/tries/compressed-trie">Сжатый бор</Item>
        <Item planned>Цифровой бор</Item>
        <Item planned>X-fast и Y-fast боры</Item>
        <Item planned>DAWG и сжатый DAWG</Item>
        <Item planned>Judy Array</Item>
    </Category>

    <Category title="Хеширование">
        <Item planned>Числовое хеширование</Item>
        <Item link="/search/hashing/polynomial">Полиномиальное хеширование</Item>
        <Item planned>Хеш-таблицы</Item>
        <Item link="/search/hashing/bloom-filter">Фильтр Блума</Item>
        <Item link="/search/hashing/count-sketch">Count sketch</Item>
        <Item planned>Cuckoo Filters</Item>
    </Category>

    <Category title="Finger search">
        <Item planned>Декартовы деревья</Item>
        <Item planned>Level-Linked Trees</Item>
        <Item link="/search/simple-search/skip-list">Skip list</Item>
    </Category>

    <Category title="Строки">
        <Item planned>Префикс-функция</Item>
        <Item planned>Z-функция</Item>
        <Item planned>Суффиксный бор</Item>
        <Item planned>Куча позиций</Item>
    </Category>

    <Category title="Текст">
        <Item planned>Инвертированный индекс</Item>
        <Item link="/search/text/rope">Строп</Item>
        <Item planned>Буфер с разрывом</Item>
        <Item planned>N-грамм индекс</Item>
    </Category>

    <Category title="Пространственный поиск">
        <Item planned>KD дерево</Item>
        <Item planned>R-дерево</Item>
        <Item planned>Метрические деревья</Item>
        <Item planned>Quadtree</Item>
    </Category>

    <Category title="Нечёткий поиск">
        <Item link="/search/fuzzy-search/similarity-measures">Меры схожести</Item>
        <Item planned>Locality-sensitive hashing</Item>
        <Item link="/search/fuzzy-search/bk-tree">Дерево Буркхарда&ndash;Келлера</Item>
    </Category>
</Chapter>


<Heading>Комбинаторика и комбинаторные алгоритмы</Heading>
<Chapter>
    <Category title="Основные объекты">
        <Item link="/combinatorics/basic-objects/chooses">Сочетания</Item>
    </Category>

    <Category title="База генерации и поиска">
        <Item link="/combinatorics/bases/gray-code">Код Грея</Item>
        <Item link="/combinatorics/bases/sims-table">Таблицы Симса</Item>
    </Category>

    <Category title="Семейства множеств">
        <Item link="/combinatorics/connectivity/disjoint-set-union">Система непересекающихся множеств</Item>
        <Item link="/combinatorics/connectivity/sack">Мешок</Item>
        <Item planned>Система непересекающихся множеств</Item>
    </Category>

    <Category title="Генерация комбинаторных объектов">
        <Item link="/combinatorics/generation/tuples">Генерация кортежей</Item>
        <Item planned>Генерация перестановок</Item>
        <Item planned>Генерация сочетаний</Item>
        <Item planned>Генерация разбиений чисел</Item>
        <Item planned>Генерация разбиений множеств</Item>
        <Item planned>Генерация деревьев</Item>
    </Category>

    <Category title="Отрезки и каскады">
        <Item link="/combinatorics/segments-cascades/cumulative-list">Кумулятивный список</Item>
        <Item planned>Разностный список</Item>
        <Item planned>Дерево Фенвика</Item>
        <Item planned>Дерево отрезков</Item>
    </Category>

    <Category title="Теория независимости">
        <Item planned>Матроиды</Item>
        <Item planned>Двойственность</Item>
        <Item planned>Гридоиды</Item>
    </Category>
</Chapter>

<Heading>Техники и стратегии</Heading>
<Chapter>
    <Category title="Индуктивность">
        <Item link="/techniques/inductivity/inductive-functions">Индуктивные функции</Item>
        <Item planned>Индуктивное расширение</Item>
        <Item link="/techniques/inductivity/cumulative-arrays">Кумулятивные массивы</Item>
        <Item planned>Разностные массивы</Item>
    </Category>

    <Category title="Кеширование">
        <Item link="techniques/caching/caches">Кеши</Item>
        <Item link="techniques/caching/cache-replacement-policies">Алгоритмы вытеснения кеша</Item>
    </Category>

    <Category title="Декомпозиция">
        <Item planned>Корневая декомпозиция</Item>
    </Category>

    <Category title="Отложенные вычисления">
        <Item link="techniques/lazy-evaluation/venice-technique">Венецианская техника</Item>
    </Category>

    <Category title="Персистентность">
        <Item planned>Структуры с откатами</Item>
        <Item planned>Метод копирования пути</Item>
    </Category>
</Chapter>


<Heading>Оптимизация</Heading>
<Chapter>
    <Category title="Градиентные методы">
        <Item link="/optimization/gradient-methods/gradient-descent">Градиентный спуск</Item>
    </Category>
</Chapter>


<Heading>Системное программирование</Heading>
<Chapter>
    <Category title="Данные и объекты">
        <Item link="/systems-programming/data-and-objects/serialization">Сериализация</Item>
        <Item planned>Заморозка</Item>
    </Category>

    <Category title="Программы">
        <Item planned>Streams</Item>
        <Item planned>Процессы и потоки</Item>
    </Category>

    <Category title="Память">
        <Item planned>Организация памяти</Item>
        <Item planned>Виртуальная память</Item>
    </Category>

    <Category title="Файловые системы">
        <Item planned>Файлы и папки</Item>
        <Item planned>FAT и адресация</Item>
        <Item planned>Дефрагментация</Item>
        <Item planned>NTFS</Item>
        <Item planned>RAID-массивы</Item>
    </Category>
</Chapter>


<Heading>Сети</Heading>
<Chapter>
    <Category title="...">
        <Item planned>...</Item>
    </Category>
</Chapter>


<Heading>Генерация случайностей</Heading>
<Chapter>
    <Category title="Равномерное распределение">
        <Item link="/random-generators/uniform/linear-congruential-method">Линейный конгруэнтный метод</Item>
        <Item planned>Птички</Item>
    </Category>

    <Category title="Генераторы случайных величин">
        <Item planned>Метод инверсии</Item>
        <Item planned>Метод отбрасывания</Item>
        <Item planned>Метод сжимания</Item>
        <Item planned>Дискретные смеси</Item>
    </Category>

    <Category title="Процедурная генерация">
        <Item planned>Шум Перлина</Item>
    </Category>

    <Category title="Хаос">
        <Item planned>Аттракторы</Item>
    </Category>
</Chapter>


<Heading>Графы и сети</Heading>
<Chapter>
    <Category title="Основы теории графов">
        <Item planned>Графы и операции над ними</Item>
        <Item planned>Обход в глубину</Item>
    </Category>
</Chapter>


<Heading>Кодирование</Heading>
<Chapter>
    <Category title="Алфавитное кодирование">
        <Item link="/coding/alphabetic/basics">Основы кодирования</Item>
        <Item link="/coding/alphabetic/codings">Кодировки</Item>
        <Item link="/coding/alphabetic/legacy-ciphers">Древние шифры</Item>
    </Category>

    <Category title="Оптимальное кодирование">
        <Item planned>Цена кодирования</Item>
        <Item planned>Алгоритм Фано</Item>
        <Item planned>Алгоритм Хафмана</Item>
    </Category>

    <Category title="Помехоустойчивое кодирование">
        <Item planned>Исправление ошибок</Item>
        <Item planned>Код Хемминга</Item>
        <Item planned>Алгоритм Рида-Соломона</Item>
    </Category>

    <Category title="Сжатие без потерь">
        <Item link="/coding/compression/rle">Сжатие длин серий</Item>
    </Category>

    <Category title="Сжатие с потерями">
        <Item link="/coding/compression/lossy-compression">Сжатие координат</Item>
    </Category>

    <Category title="Текстовые кодировки">
        <Item planned>Текстовые кодировки и ASCII</Item>
        <Item planned>Национальные кодировки</Item>
        <Item planned></Item>
    </Category>
</Chapter>

<Heading>Криптография</Heading>
<Chapter>
    <Category title="Основные концепции">
        <Item planned>Шифрование</Item>
        <Item planned>Аутентификация</Item>
        <Item planned>Цифровые подписи</Item>
    </Category>

    <Category title="Блочное шифрование">
        <Item planned>Блочные шифры</Item>
        <Item planned>DES</Item>
        <Item planned>AES</Item>
        <Item planned>Serpent</Item>
        <Item planned>Twofish</Item>
        <Item planned>Атака с помощью решения уравнений</Item>
    </Category>


    <Category title="Ассиметричные шифры">
        <Item link="/cryptography/asymmetric-ciphers/RSA">RSA</Item>
    </Category>

    <Category title="Криптостойкое хеширование">
        <Item planned>Безопасное хеширование</Item>
        <Item planned>MD5</Item>
        <Item planned>SHA-1</Item>
        <Item planned>SHA-256, SHA-384 и SHA-512</Item>
        <Item planned>Модификация функций хеширования</Item>
        <Item planned>Продвинутые методы хеширования</Item>
    </Category>

    <Category title="Коды аутентичности сообщений">
        <Item planned>MAC</Item>
        <Item planned>CBC-MAC</Item>
        <Item planned>HMAC и SHAd</Item>
        <Item planned>UMAC</Item>
    </Category>
</Chapter>


<Heading>Базы данных</Heading>
<Chapter>
    <Category title="Основы проектирования">
        <Item planned>Базы данных</Item>
        <Item planned>Доступ и сессии</Item>
        <Item planned>Архитектура СУБД</Item>
    </Category>

    <Category title="Реляционная модель">
        <Item planned>Структура реляционной модели</Item>
    </Category>

    <Category title="Запросы">
        <Item planned>Сессии и транзакции</Item>
        <Item planned>Конфликты</Item>
    </Category>
</Chapter>


<Heading>Вычислительная геометрия</Heading>
<Chapter>
    <Category title="Примитивы">
        <Category></Category>
    </Category>
</Chapter>


<Heading>Изображения</Heading>
<Chapter>
    <Category title="Непрерывные изображения">
        <Item planned>Дискретизация непрерывных изображений</Item>
        <Item planned>Квантование</Item>
    </Category>
</Chapter>


<Heading>Обработка сигналов</Heading>
<Chapter>
    <Category title="Основы">
        <Item planned>Цифровые сигналы. Дискретизация и квантование</Item>
        <Item planned>Линейные системы (LTI-системы)</Item>
        <Item planned>Свертка</Item>
    </Category>

    <Category title="Анализ Фурье">
        <Item planned>Преобразование Фурье</Item>
        <Item planned>Дискретное преобразование Фурье</Item>
        <Item planned>Спектральная оценка</Item>
        <Item planned>вейвлет-преобразование</Item>
    </Category>

    <Category title="Фильтрация">
        <Item planned>Скользящие окна</Item>
        <Item planned>FIR-фильтры</Item>
        <Item planned>IIR-фильтры</Item>
        <Item planned>Проектирование фильтров</Item>
        <Item planned>Адаптивная фильтрация</Item>
    </Category>

    <Category title="Регуляторы">
        <Item planned>PID-регуляторы</Item>
    </Category>
</Chapter>


<Heading>Искусственный интеллект</Heading>
<Chapter>
    <Category title="Стохастические алгоритмы">
        <Item planned>Случайный поиск</Item>
        <Item planned>Поиск с восхождением</Item>
        <Item planned>Локальный поиск</Item>
    </Category>

    <Category title="Эволюционные алгоритмы">
        <Item planned>Генетический алгоритм</Item>
        <Item planned>Стратегии эволюции</Item>
        <Item planned>Геном</Item>
    </Category>

    <Category title="Роевой интеллект">
        <Item planned>Муравьиный алгоритм</Item>
        <Item planned>Метод роя частиц</Item>
        <Item planned>Пчелиный алгоритм</Item>
    </Category>
</Chapter>


<Heading>Конкурентность и распределённые системы</Heading>
<Chapter>
    <Category title="Параллельные вычисления">
        <Category></Category>
    </Category>
</Chapter>


