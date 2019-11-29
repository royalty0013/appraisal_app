document.addEventListener("DOMContentLoaded", function(event) {
document.getElementById('row-add').onclick = function () {
    let template = `
        <TD id="Goal-td"><textarea style="width: 100%; height: 100px" name= 'objective'></textarea></TD>
                        <TD id="Goal-td"><textarea style="width: 100%; height: 100px" name= 'specific_task'></textarea></TD>
                        <TD id="Goal-td"><textarea style="width: 100%; height: 100px" name= 'achievement'></textarea></TD>
                        <TD id="Goal-td">
                            <select style="width: 100%" class="strat-focus" name='strat'>
                                <option value="Click Here">Click Here</option>
                                <option value="Reduce ATC&C Loss">Reduce ATC&C Loss</option>
                                <option value="Achieve Financial Viability">Achieve Financial Viability</option>
                                <option value="Create a Customer Centric Organization">Create a Customer Centric Organization</option>
                                <option value="Effective Regulatory & Stakeholders Engagement">Effective Regulatory & Stakeholders Engagement</option>
                                <option value="Improve HSE Practices">Improve HSE Practices</option>
                                <option value="Implement Prudent Asset Management Practices">Implement Prudent Asset Management Practices</option>
                                <option value="Deploy Fit for Purpose ICT Business Solutions">Deploy Fit for Purpose ICT Business Solutions</option>
                                <option value="Create a High Performance Culture">Create a High Performance Culture</option>
                                <option value="Compliance with Reengineered Business Processes">Compliance with Reengineered Business Processes</option>
                              </select>
                        </TD>
                        <TD id="Goal-td"><input type="text"  disabled style="width: 100%" align="Central"></TD>
                        <TD id="Goal-td" ><textarea style="width: 100%; height: 100px" name='weight'></textarea></TD>
                        <TD id="Goal-td"><textarea style="width: 100%; height: 100px" name='timeline'></textarea></TD>
                        <TD><button id="remove" value="Delete">-</button></TD>`;

    let container = document.getElementById('goals-tbody');
    let tr = document.createElement('tr');
    tr.innerHTML = template;
    container.appendChild(tr);
}
})
