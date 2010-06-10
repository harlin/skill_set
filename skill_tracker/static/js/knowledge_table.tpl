<table border=1>
	<thead>
		<tr>
		    <td> Skills/Users </td>
		    {#for index = 1 to $T.data.skill_count}
    			<td> {$T.data.skills[$T.index - 1].name} </td>
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
		        </td>
			{#/for}
	    </tr>
	    {#/for}
	</tbody>
</table>
