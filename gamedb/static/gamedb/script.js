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
      signup_username: {
        identifier: 'signup-username',
        rules: [{
          type: 'empty',
          prompt: 'Enter Username'
        }]
      },
      signup_email: {
        identifier: 'signup-email',
        rules: [{
          type: 'empty',
          prompt: 'Enter Email'
        }]
      },
      signup_password: {
        identifier: 'signup-password',
        rules: [{
          type: 'empty',
          prompt: 'Enter Password'
        }]
      },
    });

  $('.ui.to-comment.rating').rating({
    initialRating: 3,
    maxRating: 5,
    clearable: true,
    onRate: function(value) {
      $('.ui.to-comment.rating').attr('data-rating',value);
      $('.to-rate').attr('value',value);
    },
  })

  $('.ui.to-display.rating').rating({
    maxRating: 5,
  })

  $('.ui.to-display.rating') .rating('disable');

  $('.ui.icon.button').click(function () {
    document.location.href = $(this).attr("data-url");
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