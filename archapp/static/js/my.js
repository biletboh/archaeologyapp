//Dropdown for oblasti

function configureDropDownLists(ddl1,ddl2) {
  var poltavska = new Array('Великобагачанський', 'Гадяцький', 'Глобинський', 'Гребінківський', 'Диканський', 'Зіньківський', 'Карлівський', 'Кобеляцький', 'Козельщинський', 'Котелевський', 'Кременчуцький', 'Лохвицький', 'Лубенський', 'Машівський', 'Миргородський', 'Новосанжарський', 'Оржицький', 'Пирятинський', 'Полтавський', 'Решетилівський', 'Семенівський', 'Хорольський', 'Чорнухинський', 'Чутівський', 'Шишацький');
  var chernigivska = new Array('Бахмацький', ' Бобровицький', ' Борзнянський', ' Варвинський', ' Городнянський', ' Ічнянський', ' Козелецький', ' Коропський', ' Корюківський', ' Куликівський', ' Менський', ' Ніжинський', ' Новгород-Сіверський', ' Носівський', ' Прилуцький', ' Ріпкинський', ' Семенівський', ' Сосницький', ' Срібнянський', ' Талалаївський', ' Чернігівський', ' Щорський');
  var kurska = new Array('Беловский', ' Большесолдатский', ' Глушковский', ' Горшеченский', ' Дмитриевский', ' Железногорский', ' Золотухинский', ' Касторенский', ' Конышёвский', ' Кореневский', ' Курский', ' Курчатовский', ' Льговский', ' Мантуровский', ' Медвенский', ' Обоянский', ' Октябрьский', ' Поныровский', ' Пристенский', ' Рыльский', ' Советский', ' Солнцевский', ' Суджанский', ' Тимский', ' Фатежский', ' Хомутовский', ' Черемисиновский', ' Щигровский')
  var branska = new Array('Брасовский', ' Брянский', ' Выгоничский', ' Гордеевский', ' Дубровский', ' Дятьковский', ' Жирятинский', ' Жуковский', ' Злынковский', ' Карачевский', ' Клетнянский', ' Климовский', ' Клинцовский', ' Комаричский', ' Красногорский', ' Мглинский', ' Навлинский', ' Новозыбковский', ' Погарский', ' Почепский', ' Рогнединский', ' Севский', ' Стародубский', ' Суземский', ' Суражский', ' Трубчевский', ' Унечский')
  var orlovska = new Array('Болховский', ' Верховский', ' Глазуновский', ' Дмитровский', ' Должанский', ' Залегощенский', ' Знаменский', ' Колпнянский', ' Корсаковский', ' Краснозоренский', ' Кромской', ' Ливенский', ' Малоархангельский', ' Мценский', ' Новодеревеньковский', ' Новосильский', ' Орловский', ' Покровский', ' Свердловский', ' Сосковский', ' Троснянский', ' Урицкий', ' Хотынецкий', ' Шаблыкинский')
  switch (ddl1.value) {
    case 'poltavska':
      ddl2.options.length = 0;
      for (i = 0; i < poltavska.length; i++) {
        createOption(ddl2, poltavska[i], poltavska[i]);
      }
      break;
    case 'chernigivska':
      ddl2.options.length = 0; 
      for (i = 0; i < chernigivska.length; i++) {
        createOption(ddl2, chernigivska[i], chernigivska[i]);
      }
      break;
    case 'kurska':
      ddl2.options.length = 0;
      for (i = 0; i < kurska.length; i++) {
        createOption(ddl2, kurska[i], kurska[i]);
      }
      break;
      case 'branska':
      ddl2.options.length = 0; 
      for (i = 0; i < branska.length; i++) {
        createOption(ddl2, branska[i], branska[i]);
      }
      break;
      case 'orlovska':
      ddl2.options.length = 0; 
      for (i = 0; i < orlovska.length; i++) {
        createOption(ddl2, orlovska[i], orlovska[i]);
      }
      break;

    default:
      ddl2.options.length = 0;
      break;
  }

}

function createOption(ddl, text, value) {
  var opt = document.createElement('option');
  opt.value = value;
  opt.text = text;
  ddl.options.add(opt);
}

