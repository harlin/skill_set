function onKnowledgeChange(){
    var selected = $("#selected option:selected");
    if(selected.val() != 0)
    {
        $("#prompt").hide();
        $.post("/skills/knowledge/", {
                skill: selected.val()
            },
            function(responseData) {
                $("#knowledges").html(knowledgesJSONTreatment(responseData));
            }
        );
    }
}

runOnLoad(function(){
    $("#knowledge").change(onKnowledgeChange);
});
