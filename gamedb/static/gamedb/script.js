$(document).ready(function () {
    $('.ui.form')
    .form({
        gameTitle: {
        identifier: 'gameTitle',
        rules: [{
          type: 'empty',
          prompt: 'Enter a value for the Game Title'
        }]
      },
      game_type: {
        identifier: 'game_type',
        rules: [{
          type: 'empty',
          prompt: 'Enter Game Type'
        }]
      },
      release_date: {
        identifier: 'release_date',
        rules: [{
          type: 'empty',
          prompt: 'Enter Release Date'
        }]
      },
      description: {
        identifier: 'description',
        rules: [{
          type: 'empty',
          prompt: 'Enter Game Description'
        }]
      },
      made_by: {
        identifier: 'made_by',
        rules: [{
          type: 'empty',
          prompt: 'Enter Creator Company'
        }]
      },
      companyName: {
        identifier: 'companyName',
        rules: [{
          type: 'empty',
          prompt: 'Enter Company Name'
        }]
      },
      companyDescription: {
        identifier: 'companyDescription',
        rules: [{
          type: 'empty',
          prompt: 'Enter Company Description'
        }]
      },
    });

    $('.close.icon').click(function () {
      if ($('.add-attempt').length > 0) {
        $('.add-attempt').fadeOut(600, function () {
          $(this).remove();
        })
      }
    });
    
    $('.ui.dropdown').dropdown();
    $('.nav.menu .item').click(function () {
        document.location.href = $(this).attr("data-url");
    });


});