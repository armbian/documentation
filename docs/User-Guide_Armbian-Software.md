# Armbian Software

!!! warning teweew

    Following instructions are valid for next generation of Armbian config utility which is due for integration in **Armbian v24.11**. Until then please follow this installation instructions to test it out:
    <https://github.com/armbian/configng?tab=readme-ov-file#add--install-from-development-repository>

To start the Armbian software section, use the following command:
~~~
sudo armbian-config
~~~

## Adding example

### Tinkering

#### Manual install

First try to install application manually. If it works on Debian or Ubuntu, proceed. In this example we will be using `test`.

#### Clone repository

~~~
git clone https://github.com/armbian/configng
~~~

#### Design menu

Predict which commands you expect to have in the menu. For installing an application, we usually need two, `install` and `uninstall`. Armbian-config stores menu in JSON files, so you need to select appropriate file.
This one we will place under `Software -> Management`.

``` yaml title="File location: tools/json/config.software.json"
{
    "id": "MAN005",
    "description": "Webmin web-based management tool",
    "command": [
        "see_menu module_webmin"
    ],
    "status": "Stable",
    "author": "@Tearran",
    "condition": ""
}
```

| Field name | Function | Notes |
| :---------------------- | :-------------- | :----------- |
| `id` |  `unique identifier` | Select higher number. If you will select existing, application will fail to run |
| `description` |  `menu descriptor` | This will be displayed in the menu |
| `prompt` |  `confirmation text` | Some features needs confirmation before proceeding |
| `command` |  `executes function` | What should be run after we select and agree (optional) |
| `status` |  `Stable|Disabled` | Control if function is shown to users in the menu |
| `author` |  `GitHub handle` | Developer or maintainer of this functionality |
| `condition` |  `controlling display` | Under what conditions we show this menu item |


!!! note

    Pay attention to JSON structure. JSON validator at pull request will break in case spaces or commas will be placed wrong.

#### Module code

Place module functions, each into its file, following by file naming convention, into one of the folders:

``` bash title="Folder location: tools/modules"
docs
functions
network
runtime
software
system
```

``` bash title="File location: tools/modules/software/install_portainer.sh"

declare -A module_options
module_options+=(
	["module_template,author"]="@armbian"
	["module_template,feature"]="module_template"
	["module_template,example"]="install remove help"
	["module_template,desc"]="Example module unattended interface."
	["module_template,status"]="review"
)

function module_template() {
	local title="test"
	local condition=$(which "$title" 2>/dev/null)

	# Convert the example string to an array
	local commands
	IFS=' ' read -r -a commands <<< "${module_options["module_template,example"]}"

	case "$1" in
		"${commands[0]}")
		echo "Installing $title..."
		# Installation logic here
		;;
		"${commands[1]}")
		echo "Removing $title..."
		# Removal logic here
		;;
		"${commands[2]}")
			echo -e "\nUsage: ${module_options["module_template,feature"]} <command>"
			echo -e "Commands:  ${module_options["module_template,example"]}"
			echo "Available commands:"
			echo -e "\tinstall\t- Install $title."
			echo -e "\tremove\t- Remove $title."
			echo
		;;
		*)
		${module_options["module_template,feature"]} ${commands[2]}
		;;
	esac
	}

# uncomment to test the module
#module_template "$1"

```

!!! note

    Pay attention to [coding style structure](https://github.com/armbian/configng/blob/main/.editorconfig). If you use modern IDE, this will be done automatically. 

#### Manual testing

Whenever you are making changes to the JSON or modules structure, make sure to join JSON segments into main JSON file and fun. This you do with a command:
``` python
tools/config-assemble.sh -p
```
Python is required to run this tool.

``` bash
sudo sudo bin/armbian-config --cmd
```

#### Unit tests

This part is optional but highly recommended for at least install functionality. Our CI infrastructure will test this feature at pull request, on general code changes (push to main branch) and daily. It will test feature on latest Debian and Ubuntu images.
Unit tests have simple design:

Name of the config file is function id (unique identifier) `CON004.conf`

``` bash title="File location: tests/CON004.conf"
ENABLED=true
RELEASE="bookworm:jammy:noble"
CONDITION="test=\$(docker container ls -a |  grep portainer )"
```
Make sure to add a test condition that makes sense. It has to return 0 when test succeeds and 1 if fails.

| Variable | Function | Description |
| :---------------------- | :-------------- | :-------------- |
| ENABLED | false / true | If test is live or not |
| PREINSTALL | cmd to run | specific test dependencies |
| CONDITION | main test verification | must return 0 for test success |
| RELEASE  | bookworm:jammy:noble" | run on specific or leave empty to run on all |

#### Pull request

When your solution works locally and you prepare unit tests its time to submit a pull request. Fix your code and unit tests until all pull request checks becomes green.

Examples:

- <https://github.com/armbian/configng/pull/210>
- <https://github.com/armbian/configng/pull/230>

### Documentation

Documentation is generated automatically after your pull request is merged. But as automated documentation might not be satisfactory, you can add cover image, header and footer. You can use markdown elements with enhancements from https://squidfunk.github.io/mkdocs-material/

#### Cover image

Once code works perfectly, look for cover image. It can be .png or .webp. Place image to the `tools/include/images/CON004.webp`

#### Header

``` text title="Header: tools/include/markdown/CON004-header.md"
Portainer simplifies your Docker container management via Portainer web interface. It enables faster deploy of the applications and it gives real time visibility.
```

#### Footer

``` text title="Footer: tools/include/markdown/CON004-footer.md"

=== "Access to the web interface"

    The web interface is accessible via port **9002**:

    - URL = `http://<your.IP>:9002`
```
