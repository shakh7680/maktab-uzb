

const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

// School names
$(document).on('change', '.school_type', function(){
  var region = $(".region").find(':selected').val();
  var school_type_det = $('.school_type').find(':selected').val();

  $.ajax({
    url: `/schools/${region}/${school_type_det}/schoolname`,
    type: "GET",
    dataType: "json",
    success: function (data) {
      $(".school_name").html(makeSchoolsNameSection(data));
    },
  });
 });

let makeSchoolsNameSection = (schoolnames) => {
  text = '<option value="" selected ="true" disabled> Select School Name </option>';
  return schoolnames.reduce((text, schoolname) => {
    return (text += `<option value="${schoolname.schoolname}">
      ${schoolname.schoolname}</option>`);
  }, text);
};



setTimeout(function () {
  $("#message").fadeOut("slow");
}, 3000);

$(document).ready(function () {
  $(".phone_number").mask("+998 (00) 000 0000");
});

$("#login").css("min-height", $(window).height());
$("#register").css("min-height", $(window).height());
$(document).ready(() => {
  const backToTop = $("#backToTop");
  const amountScrolled = 300;

  $(window).scroll(() => {
    $(window).scrollTop() >= amountScrolled
      ? backToTop.fadeIn("fast")
      : backToTop.fadeOut("fast");
  });

  backToTop.click(() => {
    $("body, html").animate(
      {
        scrollTop: 0,
      },
      600
    );
    return false;
  });
});
$("#login").css("min-height", $(window).height());

$("#myModal").on("shown.bs.modal", function () {
  $("#myInput").trigger("focus");
});

$(".btn-comment").click(function () {
  let teacherId = $(this).data("id");
  let teacherName = $(this).data("name");
  let schoolId = $(this).data("school_id");

  $("#modal_teacher_id").val(teacherId);
  $("#modal_teacher_name").text(teacherName);
  $("#modal_school_id").val(schoolId);
});

$(".read_comment").click(function () {
  let teacherName = $(this).data("name");
  let teacherId = $(this).data("id");

  $("#modal_teacher_name1").text(teacherName);
  $("#modal_teacher_id1").val(teacherId);

  $.ajax({
    url: `/schools/teacher/${teacherId}/comments`,
    type: "GET",
    dataType: "json",
    success: function (data) {
      $("#teacher_comments").html(makeCommentsSection(data));
    },
  });
});
let x=1
let makeCommentsSection = (comments) => {
  return comments.reduce((text, comment,x) => {
    return (text += `<hr><p>${x+1}) ${comment.comment}</p>`);
  }, "");
};

$(".saving").click(function () {
  if (!$("#text-comment").val()) {
    alert("Comment first");
  }
});


// Rating
$(document).ready(function(){
  
  /* 1. Visualizing things on Hover - See next part for action on click */
  $('#stars li').on('mouseover', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
   
    // Now highlight all the stars that's not after the current hovered star
    $(this).parent().children('li.star').each(function(e){
      if (e < onStar) {
        $(this).addClass('hover');
      }
      else {
        $(this).removeClass('hover');
      }
    });
    
  }).on('mouseout', function(){
    $(this).parent().children('li.star').each(function(e){
      $(this).removeClass('hover');
    });
  });
  
  
  /* 2. Action to perform on click */
  $('#stars li').on('click', function(){
    var onStar = parseInt($(this).data('value'), 10); // The star currently selected
    var stars = $(this).parent().children('li.star');
    var teacherId = $(this).data("id");
    var userId = $(this).data("user_id");
    
    if(userId > 0)
    {
    for (i = 0; i < stars.length; i++) {
      $(stars[i]).removeClass('selected');
    }
    
    for (i = 0; i < onStar; i++) {
      $(stars[i]).addClass('selected');
    }
    
    $.ajax({
      url: `/schools/teacher/${teacherId}/${onStar}/ratings`,
      type: "GET",
      dataType: "json",
      success: function (data) {
        $(`#${teacherId}`).html(`<p class="card-text text-dark" id="${teacherId}"><span class="font-weight-bold"> Ranking: </span> ${data} </p>`);
      },
    });
  }
  else{
    alert("Register for giving rank!");
  }
 });


});

// Uploading images 




