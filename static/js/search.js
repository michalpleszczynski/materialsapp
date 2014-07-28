$("#search_form").on("submit", function( event ) {
        event.preventDefault();
        var query = $("#query").val();

        if(query.length>3){
            dataString = 'q=' + query;
            $.ajax({
                type: "GET",
                url: "/search/",
                data: dataString,
                success: function(response){
                    var results = [];
                    var list = document.createElement('ul');
                    $.each(response.ans, function(){
                        console.log(this);
                        var list_elem = document.createElement('li');
                        var link = document.createElement('a');
                        var linkText = document.createTextNode(this.name);

                        link.title = this.name;
                        link.href = this.type + "/detail/" + this.id;

                        link.appendChild(linkText);
                        list_elem.appendChild(link);
                        list.appendChild(list_elem);
                    });
                    var content = document.getElementById('results');
                    content.appendChild(list);
                }
            });
        }
    });