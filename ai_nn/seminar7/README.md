# Введение в нейронные сети

## Решение задания семинара 7

### Задание

Либо 1 пункт либо пункт 2.

1. Сделайте краткий обзор любой научной работы, посвящённой алгоритму для object detection, не рассматривавшемуся на уроке. Проведите анализ: чем отличается выбранная вами архитектура нейронной сети от других? В чём плюсы и минусы данной архитектуры? Какие могут возникнуть трудности при применении этой архитектуры на практике?

2. * Поиграться с кодом урока в разделе Advanced, поменять код и написать свои выводы.

### Решение

Описание алгоритма RetinaNet:

1. Время появления этого алгоритма 

RetinaNet - это алгоритм детектирования объектов, который был предложен в 2017 году в исследовательской работе "RetinaNet: Improving Object Detection by Reducing False Positives" (RetinaNet: Улучшение детектирования объектов путём уменьшения ложных тревог).

2. Внутреннее устройство и архитектура

RetinaNet использует новый подход к обучению моделей детектирования объектов, который называется Focal Loss (фокальная потеря). Focal Loss представляет собой модификацию стандартной потери cross-entropy, которая уменьшает влияние ложных тревог на обучение модели. Это достигается путем введения специального коэффициента, который уменьшает вес неправильно классифицированных примеров, которые близки к границе между классами.

RetinaNet также использует механизм Feature Pyramid Networks (FPN), который позволяет использовать функции высокого и низкого уровня для улучшения качества детектирования. FPN позволяет модели использовать как широкое, так и узкое зрение, что улучшает способность модели обнаруживать объекты разных размеров и форм.

3. Преимущества по сравнению с другими алгоритмами

RetinaNet имеет ряд преимуществ по сравнению с другими алгоритмами детектирования объектов. Во-первых, он может обнаруживать объекты с более высокой точностью, чем другие алгоритмы, такие как Faster R-CNN и YOLO. Во-вторых, RetinaNet может обнаруживать объекты с меньшим количеством ложных тревог, что делает его особенно полезным в приложениях, где ложные тревоги могут иметь серьезные последствия. Наконец, RetinaNet может использоваться в реальных приложениях, таких как автопилоты, где быстрота и точность обнаружения объектов являются критическими.

4. Недостатки алгоритма

RetinaNet имеет несколько недостатков. Во-первых, он требует огромных вычислительных ресурсов для обучения и больших объемов данных для обучения, что может быть проблемой для исследователей, которые не имеют доступа к мощным компьютерам, большим базам данным и датасетам. Во-вторых, RetinaNet может быть медленнее, чем другие алгоритмы, такие как YOLO, из-за его более сложной архитектуры. Наконец, RetinaNet может иметь трудности с обнаружением объектов, которые находятся вблизи друг от друга. Наконец, RetinaNet может иметь трудности в работе с недостаточно хорошо подготовленными данными, что может привести к недостаточной точности обнаружения объектов.