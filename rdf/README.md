<div class="section" id="module-rdf.rdf">
<span id="sansa-stack-rdf-layer"></span><h1>SANSA-Stack RDF Layer<a class="headerlink" href="#module-rdf.rdf" title="Permalink to this headline"></a></h1>
<p>Created on Fri Feb 6 18:12:29 2021</p>
<p>@author: erce</p>
<p>This class is a wrapper to use SANSA-Stack RDF layer functionalities
through Python.</p>
<p>It runs on SparkSession by importing SANSA-Stack jar with dependencies to
SparkContext then build a SparkSession with the SparkContext.</p>
<p>If Hadoop is installed in the system, it can be used to read and write data
from/to Hadoop url. From the SANSA-Stack and our documentation, default
local Hadoop url is =&gt; hdfs://localhost:54310/user/[username]
| E.g: hdfs://localhost:54310/user/erce</p>
<dl class="py class">
<dt id="rdf.rdf.Rdf">
<em class="property"><span class="pre">class</span> </em><code class="sig-prename descclassname"><span class="pre">rdf.rdf.</span></code><code class="sig-name descname"><span class="pre">Rdf</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sparkContext</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf" title="Permalink to this definition"></a></dt>
<dd><p class="rubric">Methods</p>
<table class="longtable docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 90%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.count" title="rdf.rdf.Rdf.count"><code class="xref py py-obj docutils literal notranslate"><span class="pre">count</span></code></a>()</p></td>
<td><p>Counts the triples in the Rdf object by using count function from SANSA RDF Layer.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.getTriples" title="rdf.rdf.Rdf.getTriples"><code class="xref py py-obj docutils literal notranslate"><span class="pre">getTriples</span></code></a>([size])</p></td>
<td><p>Gets the triples array with the given size from the triples that is read from the given file.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.initializeRdfReader" title="rdf.rdf.Rdf.initializeRdfReader"><code class="xref py py-obj docutils literal notranslate"><span class="pre">initializeRdfReader</span></code></a>(spark)</p></td>
<td><p>Initializes RDFReader class from SANSA RDF Layer to be used to read triples or for extended usage with deeper SANSA-Stack knowledge</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.outputExceptionLog" title="rdf.rdf.Rdf.outputExceptionLog"><code class="xref py py-obj docutils literal notranslate"><span class="pre">outputExceptionLog</span></code></a>(functionName,&nbsp;exception)</p></td>
<td><p>Exception function to print the exception and the function that throws the exception.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.printAttributesOfGivenObject" title="rdf.rdf.Rdf.printAttributesOfGivenObject"><code class="xref py py-obj docutils literal notranslate"><span class="pre">printAttributesOfGivenObject</span></code></a>(obj)</p></td>
<td><p>Prints functions of the given object by using “dir” function in Python</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.printRdfClassPackageList" title="rdf.rdf.Rdf.printRdfClassPackageList"><code class="xref py py-obj docutils literal notranslate"><span class="pre">printRdfClassPackageList</span></code></a>()</p></td>
<td><p>Prints the SANSA-Stack RDF Package list that is loaded to this python wrapper. | E.g.:  | rdf.packagesDict[“io”].RDFReader(spark).</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.printRdfIOAttributes" title="rdf.rdf.Rdf.printRdfIOAttributes"><code class="xref py py-obj docutils literal notranslate"><span class="pre">printRdfIOAttributes</span></code></a>()</p></td>
<td><p>Prints attributes of RDF/IO to see which functions can be used from SANSA rdf/io Package.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.printTripleObjectAttributes" title="rdf.rdf.Rdf.printTripleObjectAttributes"><code class="xref py py-obj docutils literal notranslate"><span class="pre">printTripleObjectAttributes</span></code></a>()</p></td>
<td><p>Prints attributes of RDF Triple Object.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.printTriples" title="rdf.rdf.Rdf.printTriples"><code class="xref py py-obj docutils literal notranslate"><span class="pre">printTriples</span></code></a>(tripleArray)</p></td>
<td><p>Prints triples as string with indexes from the given tripleArray.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.readTriples" title="rdf.rdf.Rdf.readTriples"><code class="xref py py-obj docutils literal notranslate"><span class="pre">readTriples</span></code></a>(rdfReader,&nbsp;path)</p></td>
<td><p>Reads triples by using RDFReader class from SANSA RDF Layer</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#rdf.rdf.Rdf.saveAsTextFile" title="rdf.rdf.Rdf.saveAsTextFile"><code class="xref py py-obj docutils literal notranslate"><span class="pre">saveAsTextFile</span></code></a>(rdfObject,&nbsp;outputPath)</p></td>
<td><p>Save triples as text file in small partitions.</p></td>
</tr>
</tbody>
</table>
<dl class="py method">
<dt id="rdf.rdf.Rdf.count">
<code class="sig-name descname"><span class="pre">count</span></code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.count" title="Permalink to this definition"></a></dt>
<dd><p>Counts the triples in the Rdf object by using count function from
SANSA RDF Layer.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p><strong>count</strong> – Size of the triples that is read from the given file</p>
</dd>
<dt class="field-even">Return type</dt>
<dd class="field-even"><p>int</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.getTriples">
<code class="sig-name descname"><span class="pre">getTriples</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.getTriples" title="Permalink to this definition"></a></dt>
<dd><p>Gets the triples array with the given size from the triples that
is read from the given file. Uses “take” function from SANSA RDF
Layer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>size</strong> (<em>int</em><em>, </em><em>optional</em>) – To return smaller array with given size or the whole array.
The default is 0</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>triples</strong> – Triples that is taken from the given file</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>array</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.initializeRdfReader">
<code class="sig-name descname"><span class="pre">initializeRdfReader</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">spark</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.initializeRdfReader" title="Permalink to this definition"></a></dt>
<dd><p>Initializes RDFReader class from SANSA RDF Layer to be used to read
triples or for extended usage with deeper SANSA-Stack knowledge</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>spark</strong> (<em>SparkSession</em>) – SparkSession that was built with SANSA fat-jar and necessary
configuration</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>rdfReader</strong> – RDFReader object from SANSA RDF Layer</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>RDFReader</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.outputExceptionLog">
<code class="sig-name descname"><span class="pre">outputExceptionLog</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">functionName</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">exception</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.outputExceptionLog" title="Permalink to this definition"></a></dt>
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
<dt id="rdf.rdf.Rdf.printAttributesOfGivenObject">
<code class="sig-name descname"><span class="pre">printAttributesOfGivenObject</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">obj</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.printAttributesOfGivenObject" title="Permalink to this definition"></a></dt>
<dd><dl>
<dt>Prints functions of the given object by using “dir” function in Python</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line">rdf.printAttributesOfGivenObject(rdf.packagesDict[“qualityassesment”])</div>
</div>
</dd>
</dl>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>obj</strong> (<em>Object</em>) – Any object to see the attributes and functions of it</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.printRdfClassPackageList">
<code class="sig-name descname"><span class="pre">printRdfClassPackageList</span></code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.printRdfClassPackageList" title="Permalink to this definition"></a></dt>
<dd><p>Prints the SANSA-Stack RDF Package list that is loaded to this python
wrapper.</p>
<blockquote>
<div><div class="line-block">
<div class="line">E.g.:</div>
<div class="line">rdf.packagesDict[“io”].RDFReader(spark)</div>
</div>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.printRdfIOAttributes">
<code class="sig-name descname"><span class="pre">printRdfIOAttributes</span></code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.printRdfIOAttributes" title="Permalink to this definition"></a></dt>
<dd><p>Prints attributes of RDF/IO to see which functions can be used from
SANSA rdf/io Package.</p>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.printTripleObjectAttributes">
<code class="sig-name descname"><span class="pre">printTripleObjectAttributes</span></code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.printTripleObjectAttributes" title="Permalink to this definition"></a></dt>
<dd><p>Prints attributes of RDF Triple Object. It can be used to see the
usable functions. It is possible to use functions directly with
SANSA-Stack knowledge.</p>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.printTriples">
<code class="sig-name descname"><span class="pre">printTriples</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">tripleArray</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.printTriples" title="Permalink to this definition"></a></dt>
<dd><p>Prints triples as string with indexes from the given tripleArray.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>tripleArray</strong> (<em>array</em>) – Triple array</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.readTriples">
<code class="sig-name descname"><span class="pre">readTriples</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">rdfReader</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">path</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.readTriples" title="Permalink to this definition"></a></dt>
<dd><p>Reads triples by using RDFReader class from SANSA RDF Layer</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>rdfReader</strong> (<em>RDFReader</em>) – RDFReader object from SANSA RDF Layer</p></li>
<li><p><strong>path</strong> (<em>string</em>) – </p><dl>
<dt>Path to triple file in local machine or hadoop</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/erce/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="rdf.rdf.Rdf.saveAsTextFile">
<code class="sig-name descname"><span class="pre">saveAsTextFile</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">rdfObject</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">outputPath</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rdf.rdf.Rdf.saveAsTextFile" title="Permalink to this definition"></a></dt>
<dd><p>Save triples as text file in small partitions. Uses “saveAsTextFile”
from SANSA RDF Layer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>rdfObject</strong> (<em>RDF Triple Object</em>) – Return object of SANSA RDF IO Package “rdf” function</p></li>
<li><p><strong>outputPath</strong> (<em>string</em>) – </p><dl>
<dt>Output will be a directory with several text files</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///output">file:///output</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/erce/output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
