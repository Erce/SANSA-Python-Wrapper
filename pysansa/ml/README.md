<div class="section" id="module-ml.ml">
<span id="sansa-stack-ml-layer"></span><h1>SANSA-Stack ML Layer<a class="headerlink" href="#module-ml.ml" title="Permalink to this headline"></a></h1>
<p>Created on Fri Feb 26 2021</p>
<p>@author: alex</p>
<p>This class is a wrapper to use SANSA-Stack ML layer functionalities
through Python.</p>
<p>It runs on SparkSession by importing SANSA-Stack jar with dependencies to
SparkContext then build a SparkSession with the SparkContext.</p>
<p>If Hadoop is installed in the system, it can be used to read and write data
from/to Hadoop url. From the SANSA-Stack and our documentation, default
local Hadoop url is =&gt; hdfs://localhost:54310/user/[username]
| E.g: hdfs://localhost:54310/user/alex</p>
<dl class="py class">
<dt id="ml.ml.ML">
<em class="property"><span class="pre">class</span> </em><code class="sig-prename descclassname"><span class="pre">ml.ml.</span></code><code class="sig-name descname"><span class="pre">ML</span></code><a class="headerlink" href="#ml.ml.ML" title="Permalink to this definition"></a></dt>
<dd><p class="rubric">Methods</p>
<table class="longtable docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 90%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="#ml.ml.ML.create_spark_session" title="ml.ml.ML.create_spark_session"><code class="xref py py-obj docutils literal notranslate"><span class="pre">create_spark_session</span></code></a>(sansa_jar)</p></td>
<td><p>Creates a SparkSession and loads the jar into it.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ml.ml.ML.hadoop_check" title="ml.ml.ML.hadoop_check"><code class="xref py py-obj docutils literal notranslate"><span class="pre">hadoop_check</span></code></a>(location)</p></td>
<td><p>Validates Hadoop paths, currently not in use but kept for debugging</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity" title="ml.ml.ML.ml_similarity"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity</span></code></a>(nt_file_in,&nbsp;result_folder_in,&nbsp;mode)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm with a specific mode</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity_batet" title="ml.ml.ML.ml_similarity_batet"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity_batet</span></code></a>(nt_file_in,&nbsp;result_folder_in)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm with a specific mode</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity_dice" title="ml.ml.ML.ml_similarity_dice"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity_dice</span></code></a>(nt_file_in,&nbsp;result_folder_in)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm Dice version</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity_jaccard" title="ml.ml.ML.ml_similarity_jaccard"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity_jaccard</span></code></a>(nt_file_in,&nbsp;…)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm Jaccard version</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity_minhash" title="ml.ml.ML.ml_similarity_minhash"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity_minhash</span></code></a>(nt_file_in,&nbsp;…)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm MinHash version</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity_ochiai" title="ml.ml.ML.ml_similarity_ochiai"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity_ochiai</span></code></a>(nt_file_in,&nbsp;…)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm Ochiai version</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity_simpson" title="ml.ml.ML.ml_similarity_simpson"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity_simpson</span></code></a>(nt_file_in,&nbsp;…)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm Simpson version</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ml.ml.ML.ml_similarity_tversky" title="ml.ml.ML.ml_similarity_tversky"><code class="xref py py-obj docutils literal notranslate"><span class="pre">ml_similarity_tversky</span></code></a>(nt_file_in,&nbsp;…)</p></td>
<td><p>Uses SANSA’s ML Similarity Algorithm Tversky version</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ml.ml.ML.outputExceptionLog" title="ml.ml.ML.outputExceptionLog"><code class="xref py py-obj docutils literal notranslate"><span class="pre">outputExceptionLog</span></code></a>(functionName,&nbsp;exception)</p></td>
<td><p>Exception function to print the exception and the function that throws the exception.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#ml.ml.ML.toJStringArray" title="ml.ml.ML.toJStringArray"><code class="xref py py-obj docutils literal notranslate"><span class="pre">toJStringArray</span></code></a>(arr)</p></td>
<td><p>Converts the given Stringarray into an Java String Array, to be used as input Parameter.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#ml.ml.ML.validate_arguments" title="ml.ml.ML.validate_arguments"><code class="xref py py-obj docutils literal notranslate"><span class="pre">validate_arguments</span></code></a>(source_file_in,&nbsp;…)</p></td>
<td><p>Validates input Parameters for ML-Algorithms, Hadoop and local</p></td>
</tr>
</tbody>
</table>
<dl class="py method">
<dt id="ml.ml.ML.create_spark_session">
<code class="sig-name descname"><span class="pre">create_spark_session</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sansa_jar</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.create_spark_session" title="Permalink to this definition"></a></dt>
<dd><p>Creates a SparkSession and loads the jar into it.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>sansa_jar</strong> (<em>String</em>) – Location of the Jar file, read dynamicaly by the __init__ method</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.hadoop_check">
<code class="sig-name descname"><span class="pre">hadoop_check</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">location</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.hadoop_check" title="Permalink to this definition"></a></dt>
<dd><p>Validates Hadoop paths, currently not in use but kept for debugging</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>location</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file or a folder</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
<div class="line">requires /usr/local/hadoop-2.8.3/bin/hdfs hardcoded currently, should be enhanced for further use</div>
</div>
</dd>
</dl>
<p></p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>String</strong> – dir, file or not_exists</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>String,</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity">
<code class="sig-name descname"><span class="pre">ml_similarity</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">mode</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm with a specific mode</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – Path to the nt file</p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – Path to the output folder, result will go here
Please make sure the output directory does not exist yet!</p></li>
<li><p><strong>mode</strong> (<em>String</em>) – Algorithmmode</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity_batet">
<code class="sig-name descname"><span class="pre">ml_similarity_batet</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity_batet" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm with a specific mode</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – Path to the nt file</p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – Path to the output folder, result will go here</p></li>
<li><p><strong>mode</strong> (<em>String</em>) – Algorithmmode</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity_dice">
<code class="sig-name descname"><span class="pre">ml_similarity_dice</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity_dice" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm Dice version</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the output folder, result will go here</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf_output">file:///data/rdf_output</a>  ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf_output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity_jaccard">
<code class="sig-name descname"><span class="pre">ml_similarity_jaccard</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity_jaccard" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm Jaccard version</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the output folder, result will go here</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf_output">file:///data/rdf_output</a>  ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf_output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity_minhash">
<code class="sig-name descname"><span class="pre">ml_similarity_minhash</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity_minhash" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm MinHash version</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the output folder, result will go here</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf_output">file:///data/rdf_output</a>  ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf_output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity_ochiai">
<code class="sig-name descname"><span class="pre">ml_similarity_ochiai</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity_ochiai" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm Ochiai version</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the output folder, result will go here</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf_output">file:///data/rdf_output</a>  ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf_output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity_simpson">
<code class="sig-name descname"><span class="pre">ml_similarity_simpson</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity_simpson" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm Simpson version</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the output folder, result will go here</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf_output">file:///data/rdf_output</a>  ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf_output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.ml_similarity_tversky">
<code class="sig-name descname"><span class="pre">ml_similarity_tversky</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">nt_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.ml_similarity_tversky" title="Permalink to this definition"></a></dt>
<dd><p>Uses SANSA’s ML Similarity Algorithm Tversky version</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>nt_file_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the output folder, result will go here</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf_output">file:///data/rdf_output</a>  ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf_output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.outputExceptionLog">
<code class="sig-name descname"><span class="pre">outputExceptionLog</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">functionName</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">exception</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.outputExceptionLog" title="Permalink to this definition"></a></dt>
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
<dt id="ml.ml.ML.toJStringArray">
<code class="sig-name descname"><span class="pre">toJStringArray</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">arr</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.toJStringArray" title="Permalink to this definition"></a></dt>
<dd><p>Converts the given Stringarray into an Java String Array, to be used as input Parameter.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>arr</strong> (<em>Array of Strings</em>) – e.g. [‘1’,’2’,’3’]</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>jarr</strong> – java.lang.String[] Object</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>java.lang.String[],</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="ml.ml.ML.validate_arguments">
<code class="sig-name descname"><span class="pre">validate_arguments</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">source_file_in</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">result_folder_in</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#ml.ml.ML.validate_arguments" title="Permalink to this definition"></a></dt>
<dd><p>Validates input Parameters for ML-Algorithms, Hadoop and local</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>source_file_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the nt file</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf.nt">file:///data/rdf.nt</a> ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf.nt ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
<li><p><strong>result_folder_in</strong> (<em>String</em>) – </p><dl>
<dt>Path to the output folder, result will go here</dt><dd><div class="line-block">
<div class="line">E.g.:</div>
<div class="line"><a class="reference external" href="file:///data/rdf_output">file:///data/rdf_output</a>  ===&gt; Local machine</div>
<div class="line">hdfs://localhost:54310/user/alex/rdf_output ===&gt; Hadoop</div>
</div>
</dd>
</dl>
<p></p></li>
</ul>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p><strong>error</strong> – 0 for all fine, 1 for an error. Console output</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>Integer,</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
