# :rice: Parboil

**Project Boilerplate Generator**

![GitHub](https://img.shields.io/github/license/jneug/parboil)

With _Parboil_ you can create reusable boilerplate templates to kickstart your next project.

!!! note ""

	_Parboil_ is a Python rewrite of [boilr](https://github.com/tmrts/boilr) by [Tamer Tas](https://github.com/tmrts)

----

<div data-termynal-container>
    <div id="termynal" data-termynal data-ty-typeDelay="40" data-ty-lineDelay="1500">
        <span data-ty="input">pipx install parboil</span>
        <span data-ty="progress"></span>
        <span data-ty-delay="0" data-ty>Successfully installed parboil</span>
        <span data-ty-delay="0" data-ty></span>
        <span data-ty="input" data-ty-delay="1800">boil install -d jneug/parboil-license</span>
        <span data-ty-delay="0" data-ty>[<span class="ty-success">✓</span>] Installed recipe <span class="ty-recipe">parboil-license</span></span>
		<span data-ty-delay="0" data-ty>[<span class="ty-info">i</span>]</span>
    	<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;Use with <span class="ty-cmd">boil use parboil-license</span></span>
		<span data-ty></span>
		<span data-ty="input">boil use parboil-license</span>
		<!-- -->
		<span data-ty-delay="0" data-ty>[<span class="ty-success">i</span>] Used prefilled value for "<span class="ty-ingredient">Author</span>"</span>
		<span data-ty-delay="0" data-ty>[<span class="ty-success">i</span>] Used prefilled value for "<span class="ty-ingredient">Email</span>"</span>
		<!-- -->
		<span data-ty>[<span class="ty-question">?</span>] Enter a value for "<span class="ty-ingredient">Year</span>" <span class="ty-default">(2022)</span>:</span>
		<!-- -->
		<span data-ty-delay="0" data-ty>[<span class="ty-question">?</span>] Choose a value for "<span class="ty-ingredient">License</span>"</span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">1</span> - <span class="ty-keyword">Apache License 2.0</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">2</span> - <span class="ty-keyword">MIT</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">3</span> - <span class="ty-keyword">ISC</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">4</span> - <span class="ty-keyword">GNU GPL v3.0</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">5</span> - <span class="ty-keyword">GNU GPL v2.0</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">6</span> - <span class="ty-keyword">CC-BY 4.0</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">7</span> - <span class="ty-keyword">CC-BY-SA 4.0</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ty-input">8</span> - <span class="ty-keyword">CC-0 1.0</span></span>
		<span data-ty-delay="0" data-ty>&nbsp;&nbsp;&nbsp;&nbsp;Select from <span class="ty-input">1..9</span></span>
		<span data-ty="input">2</span>
		<!-- -->
		<span data-ty>[<span class="ty-success">i</span>] Generated project for recipe "<span class="ty-recipe">parboil-license</span>" in <span class="ty-path">/Users/xyz/Projects/foo</span></span>
    </div>
</div>

## Installation

Install **Python 3** and then _Parboil_ with **pip**:

```
pip install parboil
```

_Parboil_ will install a `boil` command on your system. Run `boil --version` to see, if it worked.

## Getting started

Use `boil --help` to see the list of [available commands](overview.md) and `boil <command> --help` to see usage information for any command.

### Installing your first template

_Parboil_ maintains a local repository of project templates. To use _Parboil_ you first need to install a template. You can install templates from a local directory or download them from GitHub.

For your first template install `jneug/parboil-template` from GitHub - a project template to create parboil project templates.

```
boil install -d jneug/parboil-template pbt
```

This will download the template from [`jneug/parboil-template`](https://github.com/jneug/parboil-template) and makes it available under the name `pbt`. (The `-d` flag tells Parboil, that you want to download from GitHub and not from a local directory.)

Verify the install with `boil list`.

### Using a template

To use your new template run

```
boil use pbt new_template
```

This will create the boilerplate project in the `new_template` directory. (Omitting the directory will add the template to the current working dir.) _Parboil_ asks you to input some data and then writes the project files.

### Uninstall and update

To remove a template run `boil uninstall <templatename>` and to update from its original source (either a local directory or a GitHub repository) run `boil update <templatename>`. 

### Creating your first recipe

The `parboil-template` is a good starting point to create your own template. _Parboil_ uses [Jinja2](https://jinja.palletsprojects.com) to parse the template files and dynamically insert the user information into the template files. That means, you can use all of Jinjas features (and some more), to create your template files. 

Let's create a simple project template for meeting logs from scratch.

First, create a directory for your new template. Let's call it `meeting_log`. Then creat a directory called `template` and a file called `project.json` in it.

```
meeting_log/
├── template/
└── parboil.json
```

This is the basic structure of a parboil recipe. `parboil.json` holds the recipe configuration and `template` the actual template files.

Now open `parboil.json` in any editor and copy the following text into it:

!!! example

	``` json
	{
		// Ingredients for the meeting log recipe
		"Author": "",
		"Meeting": "Daily meeting",
		"MeetingNo": 1,
		"Topic": "Planning the day",
		"IamModerator": false,
		"NumberOfTops": 2
	}
	```

This is a basic recipe that defines five [ingredients](recipes/ingredients.md). Ingredients are essentially variables that are filled in by the user and inserted into the template files. The key of each entry is the field name, the value is the default. An empty string means, the key is required everytime.

!!! tip

	As you can see in the example above, a recipe is defined in json with comments format. 

Now we need to add the file(s) that should be created by Parboil. Create `{{Meeting}}_log.md` in the `template` directory. And enter this text:

``` jinja
# Meeting notes for {{ Meeting|title }} #{{ MeetingNo }} 

> Date: {% time '%Y-%m-%d' %}
> Topic: {{ Topic }}
> Author: {{ Author }}
{% if IamModerator %}> Moderator: {{ Author }}{% endif %}

## Topics

{% for t in range(NumberOfTops) %}
{{t|format('{:<2}')}}. 
{% endfor %}

## Notes


```

The template uses [Jinjas syntax](https://jinja.palletsprojects.com/en/3.10.x/templates/) to add the field values. For example `{{ Author }}` will be replaced with the name you entered while prompted. Note that you can use the fields in filenames, too.

You can use any Jinja [macros](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures) and [filters](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters) in your templates. `{{ Meeting|title }}` will tranform the value of "Meeting" into titlecase. `{% if IamModerator %}` is a conditional. 

For more information read [the wiki page on template creation](recipes/howto.md).

### Some more template creation

You can do some more complex stuff with templates. For example you might want to name the logfile in the example above with the current date and the meetings number padded with zeros to two digits. Also, the meeting name should be filtered for use in filenames. You would need to name the file like this:

```
{% time '%Y-%m-%d' }_{{ '{:02}'.format(MeetingNo) }}-{{ Meeting|fileify }}.md
```

The use of special chars works on many systems, but now all. Also, the filename becomes hard to read.

To deal with this, you can rename your files from the `project.json` config file. Add a `files` object next to the `fields` and map the filenames to the rename pattern:


```
{
	"fields": {
		...
	},
	"files": {
		"meeting-log.md": "{% time '%Y-%m-%d' }_{{ '{:02}'.format(MeetingNo) }}-{{ Meeting|fileify }}.md"
	}
}
```

Now you can name the log file `meeting-log.md` and will get something like `2021-03-10_04-Daily Standup.md` as a result.

There are some more features for creating complex templates, like subtemplates (for example run a template to generate a license file inside differnt app project templates), selective file inclusion, template inheritance or dealing with empty files.
