all: sponsors-profile.md

sponsors-profile.md: ../Adjoint\ School\ 2025/Application\ Form.md ../Widip/Widip.md ../Widip/WidiTalk.md ../MLIR\ Inet\ Dialect/Open\ Design\ Meeting.md make-sponsors-profile.md
	ollama run llama3.2 '$(subst ',",$(shell cat ../Adjoint\ School\ 2025/Application\ Form.md ../Widip/Widip.md ../Widip/WidiTalk.md ../MLIR\ Inet\ Dialect/Open\ Design\ Meeting.md make-sponsors-profile.md))' > $@
