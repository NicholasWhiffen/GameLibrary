"use strict";

$(document).ready( () => {
	
	$("#addSubmit").click( evt => {

		//Trim textbox values
		
		const title = $("#addTitle").val().trim();
		const console = $("#addConsole").val().trim();
		const year = $("#addYear").val().trim();
		const completed = $("#addCompleted").val().trim();
        const rating = $("#addRating").val().trim();

		//Validate info
		let isValid = true;

		if (title == ""){
			$("#addTitle").next().text("This field is required.");
            isValid = false;
		} else {
			$("#addTitle").next().text("");
			$("#addTitle").val(title);
		}
        if (console == ""){
			$("#addConsole").next().text("This field is required.");
            isValid = false;
		} else {
			$("#addConsole").next().text("");
			$("#addConsole").val(console);
		}
        if (year == ""){
			$("#addYear").next().text("This field is required.");
            isValid = false;
		} else {
			$("#addYear").next().text("");
			$("#addYear").val(year);
		}
        if (completed == ""){
			$("#addCompleted").next().text("This field is required.");
            isValid = false;
		} else {
			$("#addCompleted").next().text("");
			$("#addCompleted").val(completed);
		}
        if (rating == ""){
			$("#addRating").next().text("This field is required.");
            isValid = false;
		} else {
			$("#addRating").next().text("");
			$("#addRating").val(rating);
		}
        if (!isValid) {
            evt.preventDefault();				
        }
	});

    $("#updateSubmit").click( evt => {

		//Trim textbox values
		
		const title = $("#updateTitle").val().trim();
		const console = $("#updateConsole").val().trim();
		const year = $("#updateYear").val().trim();
		const completed = $("#updateCompleted").val().trim();
        const rating = $("#updateRating").val().trim();

		//Validate info
		let isValid = true;

		if (title == ""){
			$("#updateTitle").next().text("This field is required.");
            isValid = false;
		} else {
			$("#updateTitle").next().text("");
			$("#updateTitle").val(title);
		}
        if (console == ""){
			$("#updateConsole").next().text("This field is required.");
            isValid = false;
		} else {
			$("#updateConsole").next().text("");
			$("#updateConsole").val(console);
		}
        if (year == ""){
			$("#updateYear").next().text("This field is required.");
            isValid = false;
		} else {
			$("#updateYear").next().text("");
			$("#updateYear").val(year);
		}
        if (completed == ""){
			$("#updateCompleted").next().text("This field is required.");
            isValid = false;
		} else {
			$("#updateCompleted").next().text("");
			$("#updateCompleted").val(completed);
		}
        if (rating == ""){
			$("#updateRating").next().text("This field is required.");
            isValid = false;
		} else {
			$("#updateRating").next().text("");
			$("#updateRating").val(rating);
		}
        if (!isValid) {
            evt.preventDefault();				
        }
	});
}); // end ready