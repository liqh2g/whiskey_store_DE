### create a new repository on the command line:
    echo "# whiskey_store_DE" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/liqh2g/whiskey_store_DE.git
    git push -u origin main

### push an existing repository from the command line
    git remote add origin https://github.com/liqh2g/whiskey_store_DE.git
    git branch -M main
    git push -u origin main

---
    git status: xem trạng thái thay đổi của các file

    git log --oneline

### Eg: 
##### Bước 1: Đầu tiên clone project từ Remote Repository về Local Repository nơi mà bạn muốn lưu trên máy 

    git clone <git_remote_url> 
##### Bước 2: Sau đó vào folder của project bắt đầu ta tạo file .git để quản lý toàn bộ lịch sử Git

    git init 
##### Bước 3: Tạo một nhánh mới từ nhánh master hoặc develop

    git checkout -b <name_new_branch>
##### Bước 4: Bạn sẽ làm việc thêm, sửa, xoá tại nhánh đó 

##### Bước 5: Sau khi hoàn thành công việc bạn phải cập nhật vào Staging Area

    git add .
##### Bước 6: Commit cập nhật sự thay đổi lên Local Repository

    git commit -m <noi_dung_commit>
##### Bước 7: Push đẩy ngược code lên Remote Repository

    git push <remote> <branch>
##### remote ở đây nếu không thay đổi thì sẽ là origin

---

##### repository: là kho chứa, lưu trữ source code.
- Local: là repository được lưu tại máy tính cá nhân -  có thể thêm, sửa, xóa file, tạo "commit" để lưu lại nhưng chưa thể chia sẻ cho người khác đươc. Để tạo local repository, tại folder chứa source, thực hiện:
					> git init
			--> như vậy ta đã hiểu git init dùng cho việc gì rồi nha.
			--> tạo một local repository từ server repository:
					> git clone repository_url : Clone một Repo đã tồn tại trên GitHub, bao gồm tất cả các files, branches và commits.
- Server: cái này được lưu tại server của các hosting-service sử dụng git như Github, Gitlab, Bitbucker,...Để tạo server repository thì đơn giản là lên các web của hosting-server đó và tạo repo thôi.

##### Commit: trên mỗi branch mà ta làm việc, khi sửa đổi các file source code... Những thay đổi này cần được lưu lại bằng cách tạo ra 1 điểm mốc đánh dấu. Điểm đánh dấu các thay đổi này gọi là commit. Tại mỗi commit, git chụp lại toàn bộ dữ liệu, tại mỗi commit, git chụp lại toàn bộ dữ liệu, tạo ra 1 snapshot version hóa dữ liệu.
--> một version mới được tạo ra bằng cách tạo 1 commit cho các sửa đổi của dữ liệu.
	--> mỗi commit bao gồm 1 số thông tin sau:
			*Tên và email của người tọa commit
			*Ngày giờ tạo
			*Message: mô tả việc sửa đổi
			...
	--> làm việc với commit:
		1. Tạo commit lưu lại thay đổi:
			# Cú pháp: git commit -m <message>
				> git commit -m "Message mô tả thay đổi"

			# Lưu lại thay đổi nhưng ghi đè lên commit trước đó:
				> git commit --amend -m "Message mô tả thay đổi"

			# Ghi đè commit trước đó và đổi người tạo commit:
			# git commit --amend --author "Your name <your email>" # Chú ý ghi cả dấu < > trong case này.
				> git commit --amend --author "Nguyen Huu Kim <nguyen.huu.kim@framgia.com>"
		2. xem lại danh sách n các commit tạo gần đây:
			# Cú pháp: git log -<n>
				> git log -5
			# Hiển thị mỗi commit trên một dòng
				> git log --oneline -5
		3. So sánh các thay đổi của code trước khi add thay đổi vào commit:
				> git diff
		4.Tạo commit vào message trên nhiều dòng (mặc định chỉ trên một dòng), sử dụng dấu ' thay thế " khi tạo message:
				> git commit -m '- First line
				> - Second line'

			
			