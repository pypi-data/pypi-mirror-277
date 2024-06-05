//
// Test consistent behavior of outputs
//
casper.notebook_test(function () {

    function get_outputs(cell_idx) {
        var outputs_json = casper.evaluate(function (cell_idx) {
            var cell = Jupyter.notebook.get_cell(cell_idx);
            return JSON.stringify(cell.output_area.outputs);
        }, {cell_idx: cell_idx});
        return JSON.parse(outputs_json);
    }

    this.wait_for_kernel_ready();

    //By assigning this here we speed up the test slightly by not requiring a later this.then block
    var uuid = '';

    this.evaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 0);
        var cell = Jupyter.notebook.get_cell(0);
        uuid = cell.uuid;
        cell.set_text('def foo(x, y):\n\tglobal a\n\ta=42\n\tx,y = y,x\n\tb=10\na, b, x, y = 1,15,3,4\nfoo(17,4)\nprint(a, b, x, y)\na, b, x, y');
        cell.execute();
    });

    this.wait_for_output(0);

    this.then(function () {
        var outputs = get_outputs(0);
        this.test.assertEquals(outputs.length, 5, 'cell 0 has the right number of outputs');
        this.test.assertEquals(outputs[0].text,'1 15 3 4\n', 'cell 0 has the right number of outputs');
    });

    this.evaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 1);
        var cell = Jupyter.notebook.get_cell(1);
        cell.set_text('Out['+uuid+']');
        cell.execute();
    });

    this.wait_for_output(1);

    this.then(function () {
        var outputs = get_outputs(1);
        this.test.assertEquals(outputs.length, 1, 'cell 1 has the right number of outputs');
        this.test.assertEquals(outputs[0].data['text/plain'],'(1, 15, 3, 4)', 'cell 1 contains the same result');
    });

    //test for double execution
    this.evaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 2);
        var cell = Jupyter.notebook.get_cell(2);
        cell.set_text('c=1');
        cell.execute();
    });

    this.wait_for_output(2);

    var output_copy= '';

    this.then(function () {
        var outputs = get_outputs(2);
        output_copy = outputs;
        this.test.assertEquals(outputs.length, 1, 'cell 2 has the right number of outputs before double execution');
    });

    this.then(function () {
        this.evaluate(function () {
            var cell = Jupyter.notebook.get_cell(2);
            cell.execute();
        });
    });

    this.wait_for_output(2);

    this.then(function () {
        var outputs = get_outputs(2);
        this.test.assertEquals(outputs.length, 1, 'cell 2 has the right number of outputs after double execution');
        this.test.assertEquals(outputs,output_copy,"cell 2 output did not change after double execution");
    });
    
});
