<table border=1>
	<thead>
		<tr>
		    <td> Skills/Users </td>
		    {#for index = 1 to $T.data.skill_count}
    			<td> 
    			    <a href="/skills/{$T.data.parent_skill}/{$T.data.skills[$T.index - 1].id}"> 
    			    {$T.data.skills[$T.index - 1].name} 
    			    </a>
    			</td>
			{#/for}
		</tr>
	</thead>
	<tbody>
	    {#for u = 1 to $T.data.user_count}
	    <tr>
	        <td> {$T.data.users[$T.u - 1].name} </td>
		    {#for s = 1 to $T.data.skill_count}
  			    <td>
    		        {#if $T.data.users[$T.u - 1].knowledges[$T.s - 1].want }
	    	            <b>
	    	        {#/if}
  	    		    {$T.data.users[$T.u - 1].knowledges[$T.s - 1].level}
	    	        {#if $T.data.users[$T.u - 1].knowledges[$T.s - 1].want }
	    	            </b>
	    	        {#/if}
	    	        {#if $T.data.users[$T.u - 1].knowledges[$T.s - 1].comment != "" }
	    	        <button>{$T.data.users[$T.u - 1].knowledges[$T.s - 1].comment}</button>
	    	        {#/if}
		        </td>
			{#/for}
	    </tr>
	    {#/for}
	</tbody>
</table>
