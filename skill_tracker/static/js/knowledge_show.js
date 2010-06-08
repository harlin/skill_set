function knowledgesJSONTreatment(json)
{
                var htmlData = "<table>";
                htmlData += "<tr>";
                htmlData += "<th>User/Skill</th>";
                for (i=0; i<json.data.skill_count; i++)
                {
                    htmlData += "<th>";
                    htmlData += json.data.skills[i].name;
                    htmlData += "</th>";
                }
                htmlData += "</tr>";
                for (j=0; j<json.data.user_count; j++)
                {
                    htmlData += "<tr>";
                    htmlData += "<td>";
                    htmlData += json.data.users[j].name;
                    htmlData += "</td>";
                    for (i=0; i<json.data.skill_count; i++)
                    {
                        htmlData += "<td>";
                        if(json.data.users[j].knowledges[i].want)
                        {
                            htmlData += "<b>";
                        }
                        htmlData += json.data.users[j].knowledges[i].level;
                        if(json.data.users[j].knowledges[i].want)
                        {
                            htmlData += "</b>";
                        }
                        htmlData += "</td>";
                    }
                    htmlData += "</tr>";
                }
                htmlData += "</table>";
                return htmlData;
}

function onSkillChange(){
    var selected = $("#skill option:selected");
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

function onSubSkillChange(){
    var selected = $("#subskill option:selected");    
    if(selected.val() != 0)
    {
        $("#prompt").hide();
        $.post("/skills/knowledge/", {
                subskill: selected.val()
            },
            function(responseData) {
                $("#knowledges").html(knowledgesJSONTreatment(responseData));
            }
        );
    }
}

runOnLoad(function(){
    $("#skill").change(onSkillChange);
    $("#subskill").change(onSubSkillChange);
});
