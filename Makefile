# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ltrillar <ltrillar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/26 00:59:41 by ltrillar          #+#    #+#              #
#    Updated: 2025/10/26 02:03:01 by ltrillar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

PYTHON 	= python3
MAIN 	= src/main.py
SRC 	= src/handlers/h_input.py \
	  		src/checks/c_input.py \
	  		src/data/d_enum.py \
	  		src/debugs/d_time.py
			
NAME	= sort_script
                                    	
binary:
	@echo Compiling..
	@uv run pyinstaller --onefile --name $(NAME) $(MAIN) > /dev/null 2>&1
	@chmod +x dist/$(NAME) && mv dist/$(NAME) .
	@rm -rf dist build __pycache__ *.spec
	@echo ""
	@echo "        ██████  ▒█████   ██▀███  ▄▄▄█████▓"
	@echo "      ▒██    ▒ ▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒"
	@echo "      ░ ▓██▄   ▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░"
	@echo "        ▒   ██▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░"
	@echo "      ▒██████▒▒░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░"
	@echo "      ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░"
	@echo "      ░ ░▒  ░ ░  ░ ▒ ▒░   ░▒ ░ ▒░    ░"
	@echo "      ░  ░  ░  ░ ░ ░ ▒    ░░   ░   ░"
	@echo "            ░      ░ ░     ░"
	@echo ""

clean:
	@echo Cleaning "__pycache__"
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo Cleaning "*.pyc"
	@find . -type f -name "*.pyc" -delete
	@rm sort_script
	@echo Cleaning executable

re: clean binary

.PHONY: binary clean re