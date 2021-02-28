<div class="section" id="module-query.query">
<span id="sansa-stack-query-layer"></span><h1>SANSA-Stack Query Layer<a class="headerlink" href="#module-query.query" title="Permalink to this headline"></a></h1>
<p>Created on Fri Feb 10 22:45:51 2021</p>
<p>@author: erce</p>
<p>This class is a wrapper to use SANSA-Stack Query layer functionalities
through Python.</p>
<p>It runs on SparkSession by importing SANSA-Stack jar with dependencies to
SparkContext then build a SparkSession with the SparkContext.</p>
<p>If Hadoop is installed in the system, it can be used to read and write data
from/to Hadoop url. From the SANSA-Stack and our documentation, default
local Hadoop url is =&gt; hdfs://localhost:54310/user/[username]
| E.g: hdfs://localhost:54310/user/erce</p>
<dl class="py class">
<dt id="query.query.Query">
<em class="property"><span class="pre">class</span> </em><code class="sig-prename descclassname"><span class="pre">query.query.</span></code><code class="sig-name descname"><span class="pre">Query</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sparkContext</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query" title="Permalink to this definition"></a></dt>
<dd><p class="rubric">Methods</p>
<table class="longtable docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 90%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="#query.query.Query.convertToDataFrame" title="query.query.Query.convertToDataFrame"><code class="xref py py-obj docutils literal notranslate"><span class="pre">convertToDataFrame</span></code></a>(obj)</p></td>
<td><p>Converts object to DataFrame</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#query.query.Query.count" title="query.query.Query.count"><code class="xref py py-obj docutils literal notranslate"><span class="pre">count</span></code></a>(obj)</p></td>
<td><p>Counts DataFrame rows</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#query.query.Query.createAndGetDataLakeObject" title="query.query.Query.createAndGetDataLakeObject"><code class="xref py py-obj docutils literal notranslate"><span class="pre">createAndGetDataLakeObject</span></code></a>(query)</p></td>
<td><p>Creates and returns DataLake object</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#query.query.Query.getColumn" title="query.query.Query.getColumn"><code class="xref py py-obj docutils literal notranslate"><span class="pre">getColumn</span></code></a>(row,&nbsp;columnIndex)</p></td>
<td><p>Gets a column from the given row</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#query.query.Query.getRow" title="query.query.Query.getRow"><code class="xref py py-obj docutils literal notranslate"><span class="pre">getRow</span></code></a>(df,&nbsp;rowIndex)</p></td>
<td><p>Gets a row from the given DataFrame with the given row index</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#query.query.Query.outputExceptionLog" title="query.query.Query.outputExceptionLog"><code class="xref py py-obj docutils literal notranslate"><span class="pre">outputExceptionLog</span></code></a>(functionName,&nbsp;exception)</p></td>
<td><p>Exception function to print the exception and the function that throws the exception.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#query.query.Query.printAttributes" title="query.query.Query.printAttributes"><code class="xref py py-obj docutils literal notranslate"><span class="pre">printAttributes</span></code></a>(obj)</p></td>
<td><p>Prints functions of the given object by using “dir” function in Python</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#query.query.Query.printDF" title="query.query.Query.printDF"><code class="xref py py-obj docutils literal notranslate"><span class="pre">printDF</span></code></a>(rowArray)</p></td>
<td><p>Prints the DataFrame rows with indexes</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#query.query.Query.runQueryOnSparqlify" title="query.query.Query.runQueryOnSparqlify"><code class="xref py py-obj docutils literal notranslate"><span class="pre">runQueryOnSparqlify</span></code></a>(query)</p></td>
<td><p>Runs the given sparql query on Sparqlify</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#query.query.Query.runQueryWithDataLake" title="query.query.Query.runQueryWithDataLake"><code class="xref py py-obj docutils literal notranslate"><span class="pre">runQueryWithDataLake</span></code></a>(sparQLQuery,&nbsp;…)</p></td>
<td><p>Runs query with DataLake</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#query.query.Query.setTriplesToSparqlifyExecutor" title="query.query.Query.setTriplesToSparqlifyExecutor"><code class="xref py py-obj docutils literal notranslate"><span class="pre">setTriplesToSparqlifyExecutor</span></code></a>(triples)</p></td>
<td><p>Chooses Sparqlify as default and returns the object</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#query.query.Query.show" title="query.query.Query.show"><code class="xref py py-obj docutils literal notranslate"><span class="pre">show</span></code></a>(result)</p></td>
<td><p>Shows the data by using “show” function from SANSA Query package and print a table to the console.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#query.query.Query.takeFromDataFrame" title="query.query.Query.takeFromDataFrame"><code class="xref py py-obj docutils literal notranslate"><span class="pre">takeFromDataFrame</span></code></a>(df[,&nbsp;size])</p></td>
<td><p>Takes rows depending on the given size from DataFrame</p></td>
</tr>
</tbody>
</table>
<dl class="py method">
<dt id="query.query.Query.convertToDataFrame">
<code class="sig-name descname"><span class="pre">convertToDataFrame</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">obj</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.convertToDataFrame" title="Permalink to this definition"></a></dt>
<dd><p>Converts object to DataFrame</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>obj</strong> (<em>Object</em>) – Return object from runQueryOnSparqlify function</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>result</strong> – A DataFrame object</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>DataFrame</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.count">
<code class="sig-name descname"><span class="pre">count</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">obj</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.count" title="Permalink to this definition"></a></dt>
<dd><p>Counts DataFrame rows</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>obj</strong> (<em>DataFrame</em>) – A DataFrame object that is converted from Sparqlify object</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>count</strong> – Number of rows in the DataFrame</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>int</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.createAndGetDataLakeObject">
<code class="sig-name descname"><span class="pre">createAndGetDataLakeObject</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">query</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.createAndGetDataLakeObject" title="Permalink to this definition"></a></dt>
<dd><p>Creates and returns DataLake object</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>query</strong> (<em>string</em>) – Sparql query that fits to the triples</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Object that returns from SANSA Query package “DataLake” class</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>DataLake object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.getColumn">
<code class="sig-name descname"><span class="pre">getColumn</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">row</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">columnIndex</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.getColumn" title="Permalink to this definition"></a></dt>
<dd><p>Gets a column from the given row</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>row</strong> (<em>array</em>) – A row array that is taken from DataFrame</p></li>
<li><p><strong>columnIndex</strong> (<em>int</em>) – Column index in the range of the given row</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>Chosen column from the given row</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>string</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.getRow">
<code class="sig-name descname"><span class="pre">getRow</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">df</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">rowIndex</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.getRow" title="Permalink to this definition"></a></dt>
<dd><p>Gets a row from the given DataFrame with the given row index</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>df</strong> (<em>DataFrame</em>) – DataFrame object</p></li>
<li><p><strong>rowIndex</strong> (<em>int</em>) – Index of any row that is wished to be returned</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A row object chosen from the given DataFrame</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.outputExceptionLog">
<code class="sig-name descname"><span class="pre">outputExceptionLog</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">functionName</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">exception</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.outputExceptionLog" title="Permalink to this definition"></a></dt>
<dd><p>Exception function to print the exception and the function that
throws the exception.
Stops the SparkSession in case of failure as well if there are too many
SparkSessions running, creating new SparkSession in examples will fail.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>functionName</strong> (<em>string</em>) – Name of the function that throws the exception</p></li>
<li><p><strong>exception</strong> (<em>Exception</em>) – Exception object in Python</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.printAttributes">
<code class="sig-name descname"><span class="pre">printAttributes</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">obj</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.printAttributes" title="Permalink to this definition"></a></dt>
<dd><p>Prints functions of the given object by using “dir” function in Python</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>obj</strong> (<em>object</em>) – Any object to see the attributes and functions of it</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.printDF">
<code class="sig-name descname"><span class="pre">printDF</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">rowArray</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.printDF" title="Permalink to this definition"></a></dt>
<dd><p>Prints the DataFrame rows with indexes</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>rowArray</strong> (<em>DataFrame</em>) – Array that is taken with “take” function in
SANSA Query package. Return of “takeFromDataFrame” function in this
wrapper</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.runQueryOnSparqlify">
<code class="sig-name descname"><span class="pre">runQueryOnSparqlify</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">query</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.runQueryOnSparqlify" title="Permalink to this definition"></a></dt>
<dd><p>Runs the given sparql query on Sparqlify</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>query</strong> (<em>string</em>) – Sparql query that fits to the triples</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>result</strong> – Return from SANSA Query package “sparql” function</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.runQueryWithDataLake">
<code class="sig-name descname"><span class="pre">runQueryWithDataLake</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sparQLQuery</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">mappingsUrl</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">configUrl</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.runQueryWithDataLake" title="Permalink to this definition"></a></dt>
<dd><p>Runs query with DataLake</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>sparQLQuery</strong> (<em>string</em>) – </p></li>
<li><p><strong>mappingsUrl</strong> (<em>string</em>) – </p></li>
<li><p><strong>configUrl</strong> (<em>string</em>) – </p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>result</strong></p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Object</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.setTriplesToSparqlifyExecutor">
<code class="sig-name descname"><span class="pre">setTriplesToSparqlifyExecutor</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">triples</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.setTriplesToSparqlifyExecutor" title="Permalink to this definition"></a></dt>
<dd><p>Chooses Sparqlify as default and returns the object</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>triples</strong> (<em>RDF Triple object</em>) – Triple object that is returned from SANSA RDF IO Package “rdf”
function</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.show">
<code class="sig-name descname"><span class="pre">show</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">result</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.show" title="Permalink to this definition"></a></dt>
<dd><p>Shows the data by using “show” function from SANSA Query package
and print a table to the console.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>result</strong> (<em>Object</em>) – The object that is returned from runQueryOnSparqlify function</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="query.query.Query.takeFromDataFrame">
<code class="sig-name descname"><span class="pre">takeFromDataFrame</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">df</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#query.query.Query.takeFromDataFrame" title="Permalink to this definition"></a></dt>
<dd><p>Takes rows depending on the given size from DataFrame</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>df</strong> (<em>DataFrame</em>) – DataFrame object</p></li>
<li><p><strong>size</strong> (<em>int</em><em>, </em><em>optional</em>) – Size of the taken rows from DataFrame with “take” function from
SANSA Query package. The default is 0.</p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>result</strong> – Array from rows that are taken from the DataFrame</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>array</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
