function onSkillChange(){
    var selected = $("#skill option:selected");
    if(selected.val() != 0)
    {
        $("#prompt").hide();
        $("#subskill").val(0);
        $.post("/skills/knowledge/", {
                skill: selected.val()
            },
            function(responseData) {
                $("#knowledges").setTemplateURL("/static/js/knowledge_table.tpl");
                $("#knowledges").processTemplate(responseData);
            }
        );
    }
}

function onSubSkillChange(){
    var selected = $("#subskill option:selected");    
    if(selected.val() != 0)
    {
        $("#prompt").hide();
        $("#skill").val(0);
        $.post("/skills/knowledge/", {
                subskill: selected.val()
            },
            function(responseData) {
                $("#knowledges").setTemplateURL("/static/js/knowledge_table.tpl");
                $("#knowledges").processTemplate(responseData);
            }
        );
    }
}

runOnLoad(function(){
    $("#skill").change(onSkillChange);
    $("#subskill").change(onSubSkillChange);
});
